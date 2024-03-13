from logger import create_error_log

#Installs dependencies
def install_dependencies():
    import time
    import os

    print("Some dependencies are not installed. Would you like to install them?")
    if "y" in input("Y/N:  ").lower():
        print("Installing dependencies...")  

        try:
            os.system("pip install magic")
            os.system("pip install validators")
            os.system("pip install ffprobe")
            import magic, validators, ffprobe
        except:
            print("Pip may not be installed properly. Ensuring pip is installed...")
            time.sleep(3)
            
            operating_system = os.name()
            #Checks if Unix operating system. Otherwise, assumes Windows
            if operating_system == "posix":
                os.system("python3 -m ensurepip")
            else:
                os.system("python -3 -m ensurepip")

            #Tries to install modules again
            try:
                os.system("pip install magic")
                os.system("pip install validators")
                os.system("pip install ffprobe")
                import magic, validators, ffprobe
            except:
                print("Dependencies could not be installed. Dumping errors to 'error.log'")
                create_error_log()
                exit()
        
    else:
        print("Program cannot be run without dependencies installed. Exiting...")
        time.sleep(3)
        exit()

#Checks if dependencies are installed. Otherwise, installs them using install_dependencies() function
def check_for_dependencies():
    import time
    try:
        need_to_install = False
        print("Checking for dependencies...")
        time.sleep(1.5)
        import magic, validators, ffprobe
    except ModuleNotFoundError:
        need_to_install = True
        install_dependencies()
    except:
        print("Another error occurred while checking for dependencies. Dumping errors to 'error.log' and exiting...")
        create_error_log()
        time.sleep(3)
        exit()
    finally:
        if need_to_install:
            print("Dependencies installed successfully. Continuing to program...")
        else:
            print("Dependencies found. Continuing to program...")
        time.sleep(3)
