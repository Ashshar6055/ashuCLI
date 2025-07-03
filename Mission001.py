#Ashutosh CLI4
import boto3
from playsound import playsound
from dotenv import load_dotenv
import datetime
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import pyaudio
import getpass
import os
import subprocess
import speech_recognition as sr
import pyttsx3 as py
load_dotenv(dotenv_path=r"C:/Users/91914/OneDrive/Desktop/ashutosh.cli/pass.env")
cxxd=os.getenv("code")
user=os.getlogin()

load_dotenv(dotenv_path=r"C:/Users/91914/OneDrive/Desktop/ashutosh.cli/amazoncred.env")
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")


session = boto3.Session(
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

availablecommands=['whoami','date and time','clean','help','bye_bye','calculator','lf','lfd','file','Networking','crossai','AWS_services']
username=str(input("ashu-> Enter Username: "))
password=getpass.getpass("ashu-> Enter Password: ")



def speak_with_polly(text):
    try:
        polly = boto3.client('polly', region_name='us-east-1')

        response = polly.synthesize_speech(
            Text=text,
            OutputFormat='mp3',
            VoiceId='Joanna'
        )

        with open("speech.mp3", "wb") as file:
            file.write(response['AudioStream'].read())

        playsound("speech.mp3")

    except Exception as e:
        print("ashu-> Polly Error:", e)


    
def clearterminal():
    os.system('cls')
    print("ashu-> terminal cleared....")
def help():
    file=open(r"C:\Users\91914\OneDrive\Desktop\ashutosh.cli\ashuclihelpmodule.txt","r") 
    print(file.read())  
    file.close()
def bye_bye():
    confirmation=str(input("ashu-> Master you sure to power off yes or no"))
    if(confirmation.lower()=="yes"):
        os.system("shutdown-l")
    else:
        print("-> command terminated")
def exit():
    os.system('cls')
    print("ashu-> session ended")


def calculator():
    x=input("ashu-> enter an expression ")
    try:
        result=eval(x)
        print("ashu-> ",result)
    except Exception as e:
        print("ashu-> Error!",e)

def list_files_only():
    try:
        path=input("ashu-> enter path ")
        if not os.path.exists(path):
            print("ashu-> Path doesn't exist")
            return''
        for item in os.listdir(path):
            if os.path.isfile(os.path.join(path, item)):
                print(item)
    except Exception as e:
        print("Error", e)

def list_folders_only():
    try:
        path=input("ashu-> enter path ")
        if not os.path.exists(path):
            print("ashu-> Path doesn't exist")
            return''
        for item in os.listdir(path):
            if os.path.isdir(os.path.join(path, item)):
                print(item)
    except Exception as e :
        print("Error", e)

def file_operations():
    print("===========================")
    print("Inside file handling module")
    print("===========================")
    while True:
        print("=======================")
        opr=str(input("ashu-> Enter what you want to do with the file\nashu-> read for reading\nashu-> write for writing\nashu-> writeread for writing and reading\nashu-> Exit for exitting "))
        print("=======================")
        if(opr.lower()=="writeread"):
            path=str(input("ashu-> enter path of file "))
            file=open(path,"r+")
            print("ashu-> contents of file are\n",file.read())
            content=input("ashu -> enter content to write to the file ")
            file.write("\n"+content)
            file.close()

        elif(opr.lower()=="read"):
            path=str(input("-> enter path of file "))
            file=open(path,"r")
            print(file.read())
            file.close()
        elif(opr.lower()=="write"):
            content=input("ashu -> enter content to write to the file ")
            path=str(input("ashu-> enter path of file "))
            file=open(path,'w')
            file.write(content)
            file.close() 
        elif(opr.lower()=="exit"):
            print("")
            break
        

def networking():
    print("========================")
    print("Inside networking module")
    print("========================")

    print("==================================")
    print("        Available commands       ")
    print("        1:connections")
    print("        2:Myip")
    print("        3:Ping")
    print("        4.whatsrunning")
    print("        5:Hostname ")
    print("        6:SIS")
    print("        7:Tracert")
    print("        8:ArpT")
    print("        9:NetMap")
    print("        10:Exit")
    print("===================================")
    while True:
        
        cmd=input("ashu-> enter what command you want to run ")
        if(cmd.lower()=="connections"):
            subprocess.run("netstat",shell=True)
        elif(cmd.lower()=="myip"):
            subprocess.run("ipconfig",shell=True)
        elif(cmd.lower()=="ping"):
            what=str(input("ashu-> Enter what to ping "))
            subprocess.run(f"ping {what}",shell=True)
        elif(cmd.lower()=="whatsrunning"):
            subprocess.run("tasklist",shell=True)
        elif(cmd.lower()=="hostname"):
            subprocess.run("hostname",shell=True)
        elif(cmd.lower()=="sis"):
            subprocess.run("systeminfo",shell=True)
        elif(cmd.lower()=="tracert"):
            what=str(input("ashu-> Enter what to trace "))
            subprocess.run(f"tracert {what}",shell=True)
        elif(cmd.lower()=="arpt"):
            subprocess.run("arp -a",shell=True)
        elif(cmd.lower() == "netmap"):
            target = input("ashu-> Enter target (e.g., google.com or IP): ")
            subprocess.run(f'"D:\\Program Files\\nmap\\nmap.exe" {target}', shell=True)
        elif(cmd.lower()=="exit"):
            print("exitting...")
            break


def date_time():
    while True:
            print("==================")
            print("Inside date module")
            print("==================")
            print("Enter Date&time to know date and time\nDay for day of month\nMonth for month\nYear for year\nexit to stop\n")
            command1=str(input("ashu-> "))
            if(command1.lower()=="date&time"):
                print(datetime.datetime.now())
                print("\n")
            
            
            elif(command1.lower()=="day"):
                x=datetime.datetime.now()
                print(x.day)
                print(x.strftime("%A"))
                print("\n")

            
            elif(command1.lower()=="month"):
                x=datetime.datetime.now()
                print(x.month)
                print(x.strftime("%B"))
                print("\n")
            
            elif(command1.lower()=="year"):
                x=datetime.datetime.now()
                print(x.strftime("%Y"))
                print("\n")
            
            
            elif(command1.lower()=="exit"):
                break

def listen():
    while True:
        
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("ashu -> listening...!")
            audio=r.listen(source)
            try: 
                text=r.recognize_google(audio)
                print("ashu-> " + text)
                if text.lower() in ("hii","hello","hey there","hii there"):
                    speak("Hello ,welcome to Ashu CLI")
                elif any(phrase in text.lower() for phrase in ["what is your name","who are you","can you tell me your name","whats your name"]): 
                    speak("Im cross Ai an assistant built to help you with Ashu ClI")
                elif text.lower() in ("stop","end","exit","bye"):
                    speak("Got it")
                    speak("ending the session")
                    break
                elif(text.lower()=="help"):
                    speak("Opening help module")
                    help()
                elif any(phrase in text.lower() for phrase in ["what can you do","what are your made for","can you help me"]):
                    speak("Im specifically build to help you with ashu cli , i can run any command of ashu Cli for you you just have to name the command ,moreover i can help you with ashu Cli just type help and iwill open the help module ")
                elif(text.lower()=="calculator"):
                    speak("Opening calculator")
                    calculator()
                    break
                elif any(phrase in text.lower() for phrase in ["file operations","file","file handling","i want to work on files"]):
                    speak("Opening file module")
                    file_operations()
                    break
                elif(text.lower() in ("clean terminal","clear","clean")):
                    speak("Cleaning terminal...")
                    clearterminal()
                elif any(phrase in text.lower() for phrase in ["network","i want to do networking","networking","networks"]):
                    speak("Opening networking module")
                    networking()

                elif any(phrase in text.lower() for phrase in ["what is the date", "date", "date and time"]):
                    now = datetime.datetime.now()
                    print(now)
                    speak("Date and time is " + str(now.strftime("%A, %d %B %Y, %I:%M %p")))
                   
                    
                    
                
                else :
                    speak("Im sorry i didnt catch that")
             
            except sr.UnknownValueError:
                print("ashu ->sorry i was unable to understand that")
            except sr.RequestError:
                print("ashu-> Bad connection")

def speak(text):
    engine=py.init()
    engine.say(text)
    engine.runAndWait()

def listen2():
    print("Hello Im polly,how can i help you today")
    speak_with_polly("Hello Im polly,how can i help you today")
    print("Listening........")
    while True:
        
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("ashu -> listening...!")
            audio=r.listen(source)
            try: 
                text=r.recognize_google(audio)
                print("ashu-> " + text)
                if text.lower() in ("hii","hello","hey there","hii there"):
                    speak_with_polly("Hello ,welcome to Ashu CLI")
                elif any(phrase in text.lower() for phrase in ["what is your name","who are you","can you tell me your name","whats your name"]): 
                    speak_with_polly("Im cross Ai using Aws polly an assistant built to help you with Ashu ClI")
                elif text.lower() in ("stop","end","exit","bye"):
                    speak_with_polly("Got it")
                    speak_with_polly("ending the session")
                    break
                elif(text.lower()=="help"):
                    speak_with_polly("Opening help module")
                    help()
                elif any(phrase in text.lower() for phrase in ["what can you do","what are your made for","can you help me"]):
                    speak_with_polly("Im specifically build to help you with ashu cli , i can run any command of ashu Cli for you you just have to name the command ,moreover i can help you with ashu Cli just type help and iwill open the help module ")
                elif(text.lower()=="calculator"):
                    speak_with_polly("Opening calculator")
                    calculator()
                    break
                elif any(phrase in text.lower() for phrase in ["file operations","file","file handling","i want to work on files"]):
                    speak_with_polly("Opening file module")
                    file_operations()
                    break
                elif(text.lower() in ("clean terminal","clear","clean")):
                    speak_with_polly("Cleaning terminal...")
                    clearterminal()
                elif any(phrase in text.lower() for phrase in ["network","i want to do networking","networking","networks"]):
                    speak_with_polly("Opening networking module")
                    networking()

                elif any(phrase in text.lower() for phrase in ["what is the date", "date", "date and time"]):
                    now = datetime.datetime.now()
                    print(now)
                    speak_with_polly("Date and time is " + str(now.strftime("%A, %d %B %Y, %I:%M %p")))
                   
                    
                    
                
                else :
                    speak_with_polly("Im sorry i didnt catch that")
             
            except sr.UnknownValueError:
                print("ashu ->sorry i was unable to understand that")
            except sr.RequestError:
                print("ashu-> Bad connection")
def Aws_module():
    print("=================")
    print("Inside Aws Module")
    print("=================")
    print("   Available options")
    print("   1:AWS Polly")
    print("   2:Upload to S3")
    print("   3:List Ec2 instances ")
    print("   4:Delete_object")
    print("   5:Exit")
    
    while True:
        choice=input("ashu-> Enter your choice ")
        if choice.lower() in ["aws polly","polly","1"]:
            listen2()
        elif choice.lower() in ["s3","upload to s3","2"]:
            simple_storage_service()
        elif choice.lower() in ["list ec2","ec2","3"]:
            elastic_compute_cloud()
        elif choice.lower() in ["delete object","4","deleteobject"]:
            delete_s3_object()
        elif choice.lower()=="exit":
            break


def simple_storage_service():
    try:
        file_path=input("ashu-> Enter the path of file to upload ")
        bucket_name=input("ashu-> Enter the name for your s3 bucket ")
        object_name=input("ashu->Enter the name you want your file to be saved with ")

        s3=boto3.client('s3')
        s3.upload_file(file_path, bucket_name, object_name)
        print("ashu-> File uploaded sucessfully")
    except FileNotFoundError:
        print("ashu-> The file was not found/check your paths")
    except NoCredentialsError:
        print("ashu-> AWS credentials not found.")
    except Exception as e:
        print(f"ashu-> Error: {e}")


def elastic_compute_cloud():
    try:
        ec2 = boto3.client('ec2')  # This uses your default AWS region
        response = ec2.describe_instances()

        print("ashu-> EC2 Instances Info:\n")
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                instance_id = instance.get("InstanceId", "N/A")
                state = instance.get("State", {}).get("Name", "N/A")
                instance_type = instance.get("InstanceType", "N/A")
                region = ec2.meta.region_name

                print(f"Instance ID   : {instance_id}")
                print(f"State         : {state}")
                print(f"Type          : {instance_type}")
                print(f"Region        : {region}")
                print("--------------")
    except NoCredentialsError:
        print("ashu-> AWS credentials not found.")
    except Exception as e:
        print(f"ashu-> Error: {e}")

def delete_s3_object():
    try:
        bucket_name = input("ashu-> Enter the name of the S3 bucket: ")
        object_name = input("ashu-> Enter the name of the object (file) to delete: ")

        s3 = session.client('s3')
        s3.delete_object(Bucket=bucket_name, Key=object_name)

        print(f"ashu-> Object '{object_name}' deleted from bucket '{bucket_name}' successfully.")

    except Exception as e:
        print("ashu-> Error while deleting object:", e)



                
                   
                

        
if (username==user and password==cxxd):
    print("=================================")
    print("    \nUser Authenticated\n")
    print("=================================")
    print("+------------------------------------------------+")
    print("|                                                |")
    print("|   █████╗ ███████╗██╗  ██╗██╗   ██╗     ██████╗  |")
    print("|  ██╔══██╗██╔════╝╚██╗██╔╝╚██╗ ██╔╝    ██╔═══██╗ |")
    print("|  ███████║█████╗   ╚███╔╝  ╚████╔╝     ██║   ██║ |")
    print("|  ██╔══██║██╔══╝   ██╔██╗   ╚██╔╝      ██║   ██║ |")
    print("|  ██║  ██║███████╗██╔╝ ██╗   ██║       ╚██████╔╝ |")
    print("|  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝        ╚═════╝  |")
    print("|                                                |")
    print("|              A S H U   C L I                   |") 
    print("+------------------------------------------------+\n")
    print("\n======================================")
    print("          Welcome Master")
    print("          You are inside Ashutosh CLI")
    print("=======================================")
    print("===========")
    print("available commands are ",availablecommands)
    print("===========")

    

    while True:
        command=str(input("ashu-> "))
        if(command.lower()=="whoami"):
            print(user)
        elif(command.lower()=="clean"):
            clearterminal()
        elif(command.lower()=="help"):
            help()
        elif(command.lower()=="bye_bye"):
            bye_bye()
        elif(command.lower()=="exit"):
            exit()
        elif(command.lower()=="calculator"):
            calculator()
        elif(command.lower()=="lf"):
            list_files_only()
        elif(command.lower()=="lfd"):
            list_folders_only()
        elif(command.lower()=="file"):
            file_operations()
        elif(command.lower()=="networking"):
            networking()
        elif(command=="date and time"):
            date_time()
        elif(command=="aws_services"):
            Aws_module()
        elif(command.lower()=="crossai"):
            model=input("Which model you want to talk with\nAvailable options are: \n1:crossAI offline\n2:AWS Polly")
            if model.lower()=="aws polly":
                listen2()
            else:
                listen()
            
        else:
            print("ashu-> wrong command")
            confirmation=str(input("I can open help options for you, Yes or No\n"))
            if(confirmation.lower()=="yes"):
                help()
            else:
                exit()
                print("waiting for your next command")
else:
    print("Wrong Username or Password")



    

