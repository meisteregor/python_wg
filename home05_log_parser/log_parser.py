import sys

HELP_MESSAGE = """\help - выводит справку по программе
\show [program] - отобразить файл логов, если задан опциональный аргумент program, отобразить только сообщения конкретной программы.
\stat - отобразить статистику по программам: имя программы - количество строк в логе, дата первого сообщения, дата последнего сообщения
\exit - выйти из программы"""
STAT_MESSAGE = "\nYou are using {}\n\nCurrent logfile has {} records\n\nFirst record date is {}\nLast record date is {}\n\n"
EXIT_MESSAGE = "Bye!!"
UNKNOWN_BEHAVIOUR_MESSAGE = "Unknown behavior of {}, use '\help' to read manual"
NO_SUCH_RECORDS = "No records were found for {}"
HELLO_MESSAGE = "Hello, interactive mode of log_parser.py is running."

logfile = """Oct 11 06:29:45 ubuntu-xenial /usr/lib/snapd/snapd[1089]: snapmgr.go:504: DEBUG: Next refresh scheduled for 2017-10-11 15:06:59.521916388 +0000 UTC.
Oct 11 06:45:34 ubuntu-xenial kernel: [105959.767002] e1000: enp0s3 NIC Link is Down
Oct 11 18:16:22 ubuntu-xenial systemd[1]: Time has been changed
Oct 11 18:16:26 ubuntu-xenial kernel: [105965.779041] e1000: enp0s3 NIC Link is Up 1000 Mbps Full Duplex, Flow Control: RX
Oct 11 18:16:35 ubuntu-xenial systemd[1]: Created slice User Slice of ubuntu.
Oct 11 18:16:35 ubuntu-xenial systemd[1]: Starting User Manager for UID 1000...
Oct 11 18:16:35 ubuntu-xenial systemd[1]: Started Session 34 of user ubuntu.
Oct 11 18:16:35 ubuntu-xenial systemd[15992]: Reached target Sockets.
Oct 11 18:16:35 ubuntu-xenial systemd[15992]: Reached target Timers.
Oct 11 18:16:35 ubuntu-xenial systemd[15992]: Reached target Paths.
Oct 11 18:16:35 ubuntu-xenial systemd[15992]: Reached target Basic System.
Oct 11 18:16:35 ubuntu-xenial systemd[15992]: Reached target Default.
Oct 11 18:16:35 ubuntu-xenial systemd[15992]: Startup finished in 21ms.
Oct 11 18:16:35 ubuntu-xenial systemd[1]: Started User Manager for UID 1000.
Oct 11 18:16:38 ubuntu-xenial systemd[1]: Stopping User Manager for UID 1000...
Oct 11 18:16:38 ubuntu-xenial systemd[15992]: Reached target Shutdown.
Oct 11 18:16:38 ubuntu-xenial systemd[15992]: Starting Exit the Session...
Oct 11 18:16:38 ubuntu-xenial systemd[15992]: Stopped target Default.
Oct 11 18:16:38 ubuntu-xenial systemd[15992]: Stopped target Basic System.
Oct 11 18:16:38 ubuntu-xenial systemd[15992]: Stopped target Sockets.
Oct 11 18:16:38 ubuntu-xenial systemd[15992]: Stopped target Paths.
Oct 11 18:16:38 ubuntu-xenial systemd[15992]: Stopped target Timers.
Oct 11 18:16:38 ubuntu-xenial systemd[15992]: Received SIGRTMIN+24 from PID 16067 (kill).
Oct 11 18:16:38 ubuntu-xenial systemd[1]: Stopped User Manager for UID 1000.
Oct 11 18:16:38 ubuntu-xenial systemd[1]: Removed slice User Slice of ubuntu.
Oct 11 18:17:01 ubuntu-xenial CRON[16078]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Oct 11 18:20:31 ubuntu-xenial /usr/lib/snapd/snapd[1089]: snapmgr.go:422: No snaps to auto-refresh found
Oct 11 18:20:31 ubuntu-xenial snapd[1089]: 2017/10/11 18:20:31.699593 snapmgr.go:422: No snaps to auto-refresh found
Oct 11 18:43:38 ubuntu-xenial systemd[1]: Time has been changed
Oct 11 18:43:54 ubuntu-xenial systemd[1]: Created slice User Slice of ubuntu.
Oct 11 18:43:54 ubuntu-xenial systemd[1]: Starting User Manager for UID 1000...
Oct 11 18:43:54 ubuntu-xenial systemd[1]: Started Session 36 of user ubuntu.
Oct 11 18:43:54 ubuntu-xenial systemd[16082]: Reached target Timers.
Oct 11 18:43:54 ubuntu-xenial systemd[16082]: Reached target Sockets.
Oct 11 18:43:54 ubuntu-xenial systemd[16082]: Reached target Paths.
Oct 11 18:43:54 ubuntu-xenial systemd[16082]: Reached target Basic System.
Oct 11 18:43:54 ubuntu-xenial systemd[16082]: Reached target Default.
Oct 11 18:43:54 ubuntu-xenial systemd[16082]: Startup finished in 10ms.
Oct 11 18:43:54 ubuntu-xenial systemd[1]: Started User Manager for UID 1000.
Oct 11 18:47:28 ubuntu-xenial /usr/lib/snapd/snapd[1089]: snapmgr.go:504: DEBUG: Next refresh scheduled for 2017-10-12 02:22:04.664547424 +0000 UTC.
Oct 11 18:53:54 ubuntu-xenial systemd[1]: Stopping User Manager for UID 1000...
Oct 11 18:53:54 ubuntu-xenial systemd[16082]: Stopped target Default.
Oct 11 18:53:54 ubuntu-xenial systemd[16082]: Reached target Shutdown.
Oct 11 18:53:54 ubuntu-xenial systemd[16082]: Starting Exit the Session...
Oct 11 18:53:54 ubuntu-xenial systemd[16082]: Stopped target Basic System.
Oct 11 18:53:54 ubuntu-xenial systemd[16082]: Stopped target Sockets.
Oct 11 18:53:54 ubuntu-xenial systemd[16082]: Stopped target Timers.
Oct 11 18:53:54 ubuntu-xenial systemd[16082]: Stopped target Paths.
Oct 11 18:53:54 ubuntu-xenial systemd[16082]: Received SIGRTMIN+24 from PID 16205 (kill).
Oct 11 18:53:54 ubuntu-xenial systemd[1]: Stopped User Manager for UID 1000.
Oct 11 18:53:54 ubuntu-xenial systemd[1]: Removed slice User Slice of ubuntu.
Oct 11 19:17:01 ubuntu-xenial CRON[16216]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Oct 11 19:24:48 ubuntu-xenial dhclient[848]: DHCPDISCOVER on enp0s3 to 255.255.255.255 port 67 interval 3 (xid=0xbe395a2b)
Oct 11 19:24:48 ubuntu-xenial dhclient[848]: DHCPREQUEST of 10.0.2.15 on enp0s3 to 255.255.255.255 port 67 (xid=0x2b5a39be)
Oct 11 19:24:48 ubuntu-xenial dhclient[848]: DHCPOFFER of 10.0.2.15 from 10.0.2.2
Oct 11 19:24:48 ubuntu-xenial dhclient[848]: DHCPACK of 10.0.2.15 from 10.0.2.2
Oct 11 19:24:48 ubuntu-xenial dhclient[848]: bound to 10.0.2.15 -- renewal in 41078 seconds.
Oct 11 20:17:01 ubuntu-xenial CRON[16272]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Oct 11 21:17:01 ubuntu-xenial CRON[16275]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Oct 11 22:17:01 ubuntu-xenial CRON[16279]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Oct 22 17:43:53 ubuntu-xenial rsyslogd: [origin software="rsyslogd" swVersion="8.16.0" x-pid="1043" x-info="http://www.rsyslog.com"] start
Oct 22 17:43:53 ubuntu-xenial rsyslogd-2222: command 'KLogPermitNonKernelFacility' is currently not permitted - did you already set it via a RainerScript command (v6+ config)? [v8.16.0 try http://www.rsyslog.com/e/2222 ]
Oct 22 17:43:53 ubuntu-xenial rsyslogd: rsyslogd's groupid changed to 108
Oct 22 17:43:53 ubuntu-xenial rsyslogd: rsyslogd's userid changed to 104
Oct 22 17:43:53 ubuntu-xenial systemd-modules-load[403]: Inserted module 'iscsi_tcp'
Oct 22 17:43:53 ubuntu-xenial systemd-modules-load[403]: Inserted module 'ib_iser'
Oct 22 17:43:53 ubuntu-xenial loadkeys[387]: Loading /etc/console-setup/cached.kmap.gz
Oct 22 17:43:53 ubuntu-xenial systemd[1]: Started Uncomplicated firewall.
Oct 22 17:43:53 ubuntu-xenial systemd[1]: Started Set console keymap.
Oct 22 17:43:53 ubuntu-xenial systemd[1]: Started Remount Root and Kernel File Systems.
Oct 22 17:43:53 ubuntu-xenial systemd[1]: Started Create list of required static device nodes for the current kernel.
Oct 22 17:43:53 ubuntu-xenial systemd[1]: Started Load Kernel Modules.
Oct 22 17:43:53 ubuntu-xenial systemd[1]: Started Nameserver information manager.
Oct 22 17:43:53 ubuntu-xenial systemd[1]: Started LVM2 metadata daemon.
Oct 22 17:43:53 ubuntu-xenial systemd[1]: Starting Apply Kernel Variables...
Oct 22 17:43:53 ubuntu-xenial systemd[1]: Mounting FUSE Control File System...
Oct 22 17:43:53 ubuntu-xenial systemd[1]: Starting Create Static Device Nodes in /dev...
Oct 22 17:43:53 ubuntu-xenial systemd[1]: Starting udev Coldplug all Devices...
Oct 22 17:43:53 ubuntu-xenial systemd[1]: Starting Initial cloud-init job (pre-networking)...
Oct 22 17:43:53 ubuntu-xenial systemd[1]: Starting Load/Save Random Seed...
Oct 22 17:43:53 ubuntu-xenial systemd[1]: Starting Flush Journal to Persistent Storage...
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] Initializing cgroup subsys cpuset
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] Initializing cgroup subsys cpu
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] Initializing cgroup subsys cpuacct
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] Linux version 4.4.0-96-generic (buildd@lgw01-10) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.4) ) #119-Ubuntu SMP Tue Sep 12 14:59:54 UTC 2017 (Ubuntu 4.4.0-96.119-generic 4.4.83)
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-4.4.0-96-generic root=UUID=cbb93a26-29ca-4bd8-ae1a-68cc1384359a ro console=tty1 console=ttyS0
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] KERNEL supported cpus:
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000]   Intel GenuineIntel
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000]   AMD AuthenticAMD
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000]   Centaur CentaurHauls
Oct 22 17:43:53 ubuntu-xenial systemd[1]: Mounted FUSE Control File System.
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] x86/fpu: Supporting XSAVE feature 0x01: 'x87 floating point registers'
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] x86/fpu: Supporting XSAVE feature 0x02: 'SSE registers'
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] x86/fpu: Supporting XSAVE feature 0x04: 'AVX registers'
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] x86/fpu: Enabled xstate features 0x7, context size is 832 bytes, using 'standard' format.
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] x86/fpu: Using 'lazy' FPU context switches.
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] e820: BIOS-provided physical RAM map:
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] BIOS-e820: [mem 0x0000000000000000-0x000000000009fbff] usable
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] BIOS-e820: [mem 0x000000000009fc00-0x000000000009ffff] reserved
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] BIOS-e820: [mem 0x00000000000f0000-0x00000000000fffff] reserved
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] BIOS-e820: [mem 0x0000000000100000-0x000000003ffeffff] usable
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] BIOS-e820: [mem 0x000000003fff0000-0x000000003fffffff] ACPI data
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] BIOS-e820: [mem 0x00000000fec00000-0x00000000fec00fff] reserved
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] BIOS-e820: [mem 0x00000000fee00000-0x00000000fee00fff] reserved
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] BIOS-e820: [mem 0x00000000fffc0000-0x00000000ffffffff] reserved
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] NX (Execute Disable) protection: active
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] SMBIOS 2.5 present.
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] DMI: innotek GmbH VirtualBox/VirtualBox, BIOS VirtualBox 12/01/2006
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] Hypervisor detected: KVM
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] e820: remove [mem 0x000a0000-0x000fffff] usable
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] e820: last_pfn = 0x3fff0 max_arch_pfn = 0x400000000
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] MTRR default type: uncachable
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] MTRR variable ranges disabled:
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] MTRR: Disabled
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] x86/PAT: MTRRs disabled, skipping PAT initialization too.
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] CPU MTRRs all blank - virtualized system.
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] x86/PAT: Configuration [0-7]: WB  WT  UC- UC  WB  WT  UC- UC
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] found SMP MP-table at [mem 0x0009fff0-0x0009ffff] mapped at [ffff88000009fff0]
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] Scanning 1 areas for low memory corruption
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] Base memory trampoline at [ffff880000099000] 99000 size 24576
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] BRK [0x0220d000, 0x0220dfff] PGTABLE
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] BRK [0x0220e000, 0x0220efff] PGTABLE
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] BRK [0x0220f000, 0x0220ffff] PGTABLE
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] BRK [0x02210000, 0x02210fff] PGTABLE
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] RAMDISK: [mem 0x36234000-0x37111fff]
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] ACPI: Early table checksum verification disabled
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] ACPI: RSDP 0x00000000000E0000 000024 (v02 VBOX  )
Oct 22 17:43:53 ubuntu-xenial kernel: [    0.000000] ACPI: XSDT 0x000000003FFF0030 00003C (v01 VBOX   VBOXXSDT 00000001 ASL  00000061)"""
list_of_substrings = logfile.split("\n")


def non_char_cutter(str_):
    for char in str_:
        if not char.isalpha():
            str_ = str_.replace(char, "")
    return str_


def show_option(str_):
    set_of_known_programs = {non_char_cutter(_.split()[4]) for _ in list_of_substrings}
    if len(str_.split()) == 1:
        return logfile
    elif len(str_.split()) == 2:
        program_inputted = str_.split()[1]
        if program_inputted in set_of_known_programs:
            cut_list = [_ for _ in list_of_substrings if program_inputted in _.split()[4]]
            cut_str = "\n".join(cut_list)
            return cut_str
        else:
            return NO_SUCH_RECORDS.format(program_inputted)
    else:
        unknown_behaviour()


def stat_option():
    amount_of_records = len(list_of_substrings)
    first_record_date = " ".join(list_of_substrings[0].split(' ')[:3])
    last_record_date = " ".join(list_of_substrings[-1].split(' ')[:3])
    output = STAT_MESSAGE.format(
        __file__, amount_of_records, first_record_date, last_record_date)
    return output


def help_option():
    return HELP_MESSAGE


def unknown_behaviour():
    return UNKNOWN_BEHAVIOUR_MESSAGE.format(__file__)


def entry_point():
    print(HELLO_MESSAGE)
    while True:
        intercept = input("Enter an option: ")
        if intercept == "\stat":
            print(stat_option())
        elif intercept == '\help':
            print(help_option())
        elif intercept.lower().startswith("\show") and len(intercept.split()) < 3:
            print(show_option(intercept))
        elif intercept == '\exit':
            print(EXIT_MESSAGE)
            sys.exit()
        else:
            print(unknown_behaviour())


if __name__ == '__main__':
    entry_point()
