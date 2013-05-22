Rodan Plugins
=======================

This is a collection of plugins that simply wrap
Gamera plugins so that they can be used by Rodan.

If this plugin is being used in the context of Rodan development, make sure that your rodan virtual environment is active:

    $> cd $RODAN_HOME
    $> source rodan_env/bin/activate

Whenever you make changes to any of the jobs inside the rodan plugin, add new jobs or pull new changes, make sure to build rodan_plugins:

    $> cd $RODAN_PLUGINS
    $> python setup.py build

and then install rodan_plugins:

    $> sudo python setup.py install

If any changes were made to the method signature of an existing rodan_plugins job, you will need to recreate/update the particular job entry within the Job model.