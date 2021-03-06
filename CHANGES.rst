1.4.0-dev0
----------

1.3.2
-----

- *BUGFIX*: Fixed an issue with the html viewer menu positioning

1.3.1
-----

- *BUGFIX*: Fixed an issue with dropdown menus hidden by the navigation element

1.3.0
-----

- *NEW*: Prevent leaving the Part editor if changes have been made (#72)
- *NEW*: Send an optional e-mail to all users of a module when a change is made (#54)
- *NEW*: Administrative functionality for accessing all modules (#71)
- *UPDATE*: Use the crosshair cursor in the editor preview to indicate focusability (#69)
- *UPDATE*: Add tooltips to the editor menu icons (#70)
- *UPDATE*: Highlight Parts with upcoming Timed Actions (#80)
- *UPDATE*: Make PyWebTools an external dependency
- *UPDATE*: CSS/JS build are now performed using Gulp (#77)
- *UPDATE*: Improve the usability of the module status filter on the my modules page
- *UPDATE*: Added an explit "All Modules" link
- *BUGFIX*: Fixed a HTML Entity issue on the Part editor
- *BUGFIX*: Fixed a bug with the display of time-in-part statistics (#81)
- *BUGFIX*: Fixed a bug where tutors were never marked as registered to a module
- *BUGFIX*: Fixed the UTF-8 encoding issues with downloaded parts (#79)
- *BUGFIX*: Allow administrator access to module's users
- *BUGFIX*: Re-added the missing menu for the HTML viewer

1.2.5
-----

- *BUGFIX*: Fixed another bug with downloading/exporting parts where the name contains /
- *BUGFIX*: Fixed a bug with the encoding of static data in downloads

1.2.4
-----

- *BUGFIX*: Fixed a bug with downloading/exporting parts where the name contains /

1.2.3
-----

- *BUGFIX*: Remove extra &nbsp; in code blocks

1.2.2
-----

- *UPDATE*: Improved the Modules - My Modules distinction (#68)
- *UPDATE*: Update the YouTube embedding functionality (#74)
- *BUGFIX*: Correctly handle student progress on modules
- *BUGFIX*: Correctly handle parts with an empty content (#67)
- *BUGFIX*: Allow editing a module that has been archived (#65)
- *BUGFIX*: Line blocks now have the same styling as a paragraph (#73)

1.2.1
-----

- *BUGFIX*: Handle student progress where nothing has been visited

1.2.0
-----

- *NEW*: Added functionality to add pages / tasks before or after the
  current page / task
- *NEW*: Automatically center the part preview on the current cursor
  location
- *NEW*: Implement outline list numbering (#28)
- *NEW*: In the three-pane HTML editor layout, use AJAX to load tutorial
  pages
- *NEW*: Enable line-numbers in code blocks (#63)
- *NEW*: Keyboard shortcuts in the part editor (#61)
- *NEW*: Enable/disable line-wrapping in the part editor (#42)
- *NEW*: New UI for adding assets and parts in the part editor (#38)
- *NEW*: Parts can now be labelled
- *NEW*: Add assets directly in the part editor (#64)
- *NEW*: Compatible with both Python 2.7 and Python 3.5
- *NEW*: Re-worked the registration and forgotten password to use random tokens
- *NEW*: Support for quizzes
- *NEW*: Support for capturing time spent on pages (#31)
- *NEW*: Automatic linking between editor and preview (#29)
- *NEW*: Added text blocks that can be shown and hidden (#8)
- *UPDATE*: Use Kajiki as the rendering engine (#49)
- *UPDATE*: Improve caching of permission lookups (#49)
- *UPDATE*: The :asset: directive now automatically searches in all parent parts
- *UPDATE*: Simplified part structure: module, part, page
- *UPDATE*: Show an error message if the part content is broken (#62)
- *UPDATE*: Pages now also have an available/not-available status (#58)
- *UPDATE*: Timed actions are now available for pages (#58)
- *UPDATE*: No-select can now also be specified as a sourcecode option

1.1.1
-----

- *SECURITY*: Fixed an error that was allowing logged-in users to see
  any page in any tutorial
- *BUGFIX*: Double newlines are now preserved in code blocks (#55)
- *BUGFIX*: Correctly align the editor preview with the top of the editor (#53)

1.1.0
-----

- *NEW*: New "registration.domains" configuration setting that enables
  limiting registration to e-mail addresses that are within one or more
  domains (#24)
- *NEW*: Access to modules can now be restricted by password or e-mail
  domains (#23)
- *NEW*: Asset upload now supports drag and drop
- *UPDATE*: Improved rendering of blockquote elements (#32)
- *UPDATE*: For logged-in users the "My Modules" replaces "Modules" (#45)
- *UPDATE*: Improved the part editor to adapt to the browser window size (#27)
- *UPDATE*: Enable ETag handling for all assets (#47)
- *UPDATE*: Enable timed archiving (#50)
- *UPDATE*: Fixed a number of accessibility issues, particularly relating to
  the font icons.
- *UPDATE*: Allow assets in modules (#51)
- *UPDATE*: Make the filename for new assets optional to simplify creating
  assets (#40)
- *BUGFIX*: Fixed the calculation of the time-remaining string (#37)
- *BUGFIX*: Fixed deep-linking into modules the user is not registered for (#44)
- *BUGFIX*: Fixed a bug with non-text files in the three-pane display mode. 

1.0.3
-----

- *UPDATE*: Added an explicit save button on the tabbed editor (#48)
- *UPDATE*: Increased the autosave time to 10 seconds in the tabbed editor

1.0.2
-----

- *BUGFIX*: Fixed a problem with manually adding users to a module if they
  were already taking another module (#34)
- *BUGFIX*: Fixed a bug in the module download functionality (#36)
- *BUGFIX*: Fixed an information disclosure issue around non-accessible content
  being included in the download
- *BUGFIX*: Fixed an issue with null-characters in inline ReST roles (#35)
   
1.0.1
-----

- *BUGFIX*: Migrations were not being included in the distribution archive.

1.0.0
-----

- Initial version
