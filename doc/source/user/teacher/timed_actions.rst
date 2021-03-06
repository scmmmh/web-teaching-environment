Timed Actions
-------------

Timed actions allow you to specify that a specific change is made to your content
at a specific time. How frequently the system checks for timed actions to be run
depends on how the administrator configured the system. You should in general not
expect accuracy below 1 minute.

Timed actions are only available for modules and parts.

Add a new timed action
^^^^^^^^^^^^^^^^^^^^^^

To add a new timed action, select the action you wish to add and click on the
:primary_btn:`Add Action` button. Currently only the following timed action is available:

* **Change Status** - This action allows you to automatically change the :doc:`status<status>`
  of the module or part at a given time.

After clicking on the :primary_btn:`Add Action` button, you will automatically be taken
to the editing page for your new timed action.

Edit a timed action
^^^^^^^^^^^^^^^^^^^

To edit a timed action, move your mouse over the :icon:`fi-list` icon of the timed action and
click on the :dropdown_link:`Edit<fi-pencil>` item.

On the edit page you can specify the date and time that the action is to be run at and any
parameters to use when running the action (see below). If you select a date and time that is
in the past, then the action will essentially be run immediately.

Change Status action
++++++++++++++++++++

For the *Change Status* action there is only on parameter and that is the :doc:`status<status>`
that you wish to set for the module or part at the given date and time. 

Delete a timed action
^^^^^^^^^^^^^^^^^^^^^

To delete a timed action, move your mouse over the :icon:`fi-list` icon of the timed action and
click on the :dropdown_link:`Delete<fi-trash>` item. As this action cannot be undone you will
be asked to confirm it.
