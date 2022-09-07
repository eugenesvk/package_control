import sublime

from .. import text
from ..package_disabler import PackageDisabler
from .existing_packages_command import ExistingPackagesCommand


class DisablePackageCommand(ExistingPackagesCommand):

    """
    A command that adds a package to Sublime Text's ignored packages list
    """

    def action(self):
        """
        Build a strng to describe the action taken on selected package.
        """

        return "disable"

    def no_packages_error(self):
        """
        Return the error message to display if no packages are availablw.
        """

        return "There are no enabled packages to disable"

    def list_packages(self, manager):
        """
        Build a list of packages to display.

        :param manager:
            The package manager instance to use.

        :returns:
            A list of package names to add to the quick panel
        """

        packages = manager.list_all_packages()
        ignored = PackageDisabler.get_ignored_packages()
        return sorted(set(packages) - set(ignored), key=lambda s: s.lower())

    def on_done(self, manager, package_name):
        """
        Quick panel user selection handler - disables the selected package

        :param manager:
            The package manager instance to use.

        :param package_name:
            A package name to perform action for
        """

        PackageDisabler.disable_packages(package_name, 'disable')

        sublime.status_message(text.format(
            '''
            Package %s successfully added to list of disabled packages -
            restarting Sublime Text may be required
            ''',
            package_name
        ))
