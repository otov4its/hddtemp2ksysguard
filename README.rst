hddtemp to KSysGuard
====================

`hddtemp2ksysguard.py` adds hddtemp sensors to KDE KSysGuard utility.

Install
-------
1. Clone repository

    .. code-block:: bash

        $ git clone https://github.com/otov4its/hddtemp2ksysguard.git
        $ cd hddtemp2ksysguard
        $ chmod +x hddtemp2ksysguard.py

2. Configure hddtemp daemon mode.

    .. code-block:: bash

        $ sudo dpkg-reconfigure hddtemp

3. Open KSysGuard, "File->Monitor Remote Computer->Other Command",
   enter host name and `hddtemp2ksysguard.py` file location.

4. Now you can see hddtemp sensors in KDE KSysGuard utility.