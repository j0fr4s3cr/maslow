from pyfiglet import figlet_format
from datetime import datetime
import yaml
class Core:
        @staticmethod
        def version() -> str:
                return 'Beta: 0.1.0'


        def banner_maslow():
                custom =figlet_format("Maslow",font='slant',width=100)
                print(custom)
                print("By @J0fr4s3cr".rjust(35)+"\n")
                print("-"*70+"\n")
                print("Description: This tool is part of the Maslow Project dedicated for use Meraki API \n")
                print("Version: {}".format(Core.version())+"\n")
                print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
                
                
        def banner_seudonimo():
                print(("""\
                ##################################################################
                #                                                                #
                #     ____  _____ _     _____ _     ____  ____  _____ ____       #
                #    /  _ \/  __// \ |\/  __// \   /  _ \/  __\/  __//  __\      #
                #    | | \||  \  | | //|  \  | |   | / \||  \/||  \  |  \/|      #
                #    | |_/||  /_ | \// |  /_ | |_/\| \_/||  __/|  /_ |    /      #
                #    \____/\____\\__/  \____\\____/\____/\_/  \____\\_/\_ \     #     
                #                                                                #
                #                                              By @J0fr4s3cr     #
                #                                                                #   
                ##################################################################                                                                                        
                
        """))

        def message(message):
                print("-"*30+ message+"\n")
        
       