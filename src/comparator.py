"""
This module provides functionalities to comparing package versions 
and group packages by architecture.
"""


class PackagesComparer:
    """
    This class comparing package versions and group packages by architecture.
    """

    @classmethod
    def parse_version(cls, version_string):
        """
        Parse a version string into epoch, version, and release components.

        Parameters:
            version_string (str): version string to parse.

        Returns:
            tuple: tuple containing the epoch (int), version (str), and release (str).
        """
        parts = version_string.split(":")
        if len(parts) == 2:
            epoch, rest = parts
        else:
            epoch, rest = "0", parts[0]
        version, release = rest.split("-") if "-" in rest else (rest, "0")
        return int(epoch), version, release

    @classmethod
    def compare_elements(cls, element1, element2):
        """
        Compare two version of elements.

        Parameters:
            element1 (str): first element to compare.
            element2 (str): second element to compare.

        Returns:
            int: -1, 0, or 1 
        """
        if element1.isdigit() and element2.isdigit():
            return int(element1) - int(element2)
        return (element1 > element2) - (element1 < element2)

    @classmethod
    def compare_versions(cls, version1, version2):
        """
        Compare two version strings.

        Parameters:
            version1 (str): first version string.
            version2 (str): second version string.

        Returns:
            int: -1, 0, or 1
        """
        epoch1, ver1, rel1 = cls.parse_version(version1)
        epoch2, ver2, rel2 = cls.parse_version(version2)    

        if epoch1 != epoch2:
            return epoch1 - epoch2    

        for subver1, subver2 in zip(ver1.split('.'), ver2.split('.')):
            ver_comp = cls.compare_elements(subver1, subver2)
            if ver_comp != 0:
                return ver_comp    

        for subrel1, subrel2 in zip(rel1.split('.'), rel2.split('.')):
            rel_comp = cls.compare_elements(subrel1, subrel2)
            if rel_comp != 0:
                return rel_comp
        
        return 0

    @classmethod
    def group_packages_by_arch(cls, packages):
        """
        Group packages by their architecture.

        Parameters:
            packages (list): list of package dictionaries.

        Returns:
            dict: dict, keys - architectures and values - lists of packages.
        """
        grouped = {}
        for pkg in packages['packages']:
            arch = pkg['arch']
            if arch not in grouped:
                grouped[arch] = []
            grouped[arch].append(pkg)
        return grouped

    @classmethod
    def compare_arch_packages(cls, self_packages, other_packages):
        """
        Compare packages.

        Parameters:
            self_packages (dict): dict of packages grouped by name.
            other_packages (dict): dict of packages grouped by name to compare against.

        Returns:
            tuple: 3 lists containing packages.
        """
        self_only_packages = []
        other_only_packages = []
        version_diffs = []

        for name, pkg in self_packages.items():
            if name not in other_packages:
                self_only_packages.append(pkg)
            else:
                other_pkg = other_packages[name]
                ver1 = f"{pkg['epoch']}:{pkg['version']}-{pkg['release']}"
                ver2 = f"{other_pkg['epoch']}:{other_pkg['version']}-{other_pkg['release']}"
                if cls.compare_versions(ver1, ver2) < 0:
                    version_diffs.append(pkg)

        for name, pkg in other_packages.items():
            if name not in self_packages:
                other_only_packages.append(pkg)

        return self_only_packages, other_only_packages, version_diffs

    @classmethod
    def compare_packages(cls, self_branch_name, self_packages, other_branch_name, other_packages):
        """
        Compares packages between two branches for architecture.

        Parameters:
            self_branch_name (str): name of first branch.
            self_packages (list): packages of first branch.
            other_branch_name (str): name of second branch.
            other_packages (list): packages of second branch.

        Returns:
            dict: dict containing comparison results grouped by architecture.
        """
        self_grouped = cls.group_packages_by_arch(self_packages)
        other_grouped = cls.group_packages_by_arch(other_packages)
        
        results = {}
        
        all_archs = set(self_grouped.keys()).union(set(other_grouped.keys()))
        for arch in all_archs:
            self_arch_packages = {pkg['name']: pkg for pkg in self_grouped.get(arch, [])}
            other_arch_packages = {pkg['name']: pkg for pkg in other_grouped.get(arch, [])}
            
            self_only, other_only, version_diffs = cls.compare_arch_packages(self_arch_packages, other_arch_packages)
            
            results[arch] = {
                f"{self_branch_name}_only_packages": self_only,
                f"{other_branch_name}_only_packages": other_only,
                "version_diffs": version_diffs
            }
        
        return results