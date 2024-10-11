import os
import platform


def system_info():
    print(f"Platform: {os.name}")

    if os.name == "posix":
        uname_info = os.uname()
        print(f"OS: {uname_info.sysname}")
        print(f"Machine: {uname_info.machine}")

        distro_info = platform.freedesktop_os_release()
        print(f"Distro: {distro_info.get('NAME')}")
        print(f"Release: {uname_info.release}")

        print(f"Node Name: {uname_info.nodename}")

        try:
            with open("/proc/cpuinfo") as f:
                processor_info = f.readlines()
                processor = [line for line in processor_info if "model name" in line]
                print(
                    f"Processor: {processor[0].split(': ')[1].strip()}"
                    if processor
                    else "Processor: Unknown"
                )
        except Exception as e:
            print(f"Processor: Unable to retrieve information. Error: {e}")


if __name__ == "__main__":
    system_info()
