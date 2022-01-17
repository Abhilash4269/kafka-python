Prerequisite:{
    {
        download and extract Kafka 2.6.2 :{
            https://kafka.apache.org/downloads
        }
        
        install latest java sdk
        
        install python package : pip install kafka-python
        
        INFO:-FOR WINDOWS 11- get WMIC.exe and WMIC.exe.mui files.check under c/windows/system32/WBEM. if files are present already , ignore this.
    }
}


STEP 1:
run zookeeper server :open a new terminal {
    .\bin\windows\zookeeper-server-start.bat config\zookeeper.properties
}

STEP 2:
run kafka server :open a new terminal {
    .\bin\windows\kafka-server-start.bat config\server.properties
}

read all topics :open a new terminal{
    .\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092
}



