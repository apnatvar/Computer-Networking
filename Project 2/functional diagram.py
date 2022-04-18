from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import ElastiCache, DB
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.aws.blockchain import Blockchain
from diagrams.aws.blockchain import BlockchainResource
graph_attr = {
    "fontsize": "100",
    "bgcolor": "transparent"
}

with Diagram("CAR-E", show=True, direction="TB",graph_attr=graph_attr):
#with Diagram("CAR-E", show=True, graph_attr=graph_attr):

    doc = Blockchain("doc.json")
    with Cluster("validator.py"):
        validator = [ELB("sendData()"),
                     ECS("writeData()"),
                     ELB("receiveData()"),
                     ECS("client_thread()"),
                     ECS("connecToClient()"),
                     ECS("authenticate")]

    with Cluster("peer.py"):
        peer1 = [ELB("receiveData()"),
                     ECS("calculateStats()"),
                     ELB("sendNewData()"),
                     ELB("sendUpdatedData()"),
                     ECS("validateChain()"),
                     ECS("receiveOrSendData()"),
                     ECS("authenticate")]

    with Cluster("emissionsDatabase.py"):
        db = [ECS("search()"),
                ECS("add2Database()")]
        dbase = DB("userdb ro")

    with Cluster("blockchain.py"):
        blockchain = [ECS("createBlock()"),
                     ECS("proofOfWork()"),
                     ECS("newHash()"),
                     ECS("writeToFile()"),
                     ECS("getLastIndex()"),
                     ECS("getLastIndex()"),
                     ECS("getLastIndex()"),
                     ECS("execute()")]

    validator[1] >> blockchain[7]
    blockchain[7] >> blockchain[0]
    blockchain[7] >> blockchain[1]
    blockchain[7] >> blockchain[2]
    blockchain[7] >> blockchain[3]
    blockchain[7] >> blockchain[4]
    blockchain[7] >> blockchain[5]
    blockchain[7] >> blockchain[6]
    validator[5] >> validator[4] >> validator[3]
    validator[3] >> validator[2]
    validator[3] >> validator[0]
    validator[2] >> validator[1]
    db[0] >> db[1] >> dbase
    peer1[6] >> peer1[5]
    peer1[6] >> peer1[4]
    peer1[5] >> peer1[3]
    peer1[5] >> peer1[2]
    peer1[5] >> peer1[1]
    peer1[5] >> peer1[0]
    peer1[4] >> doc
    blockchain[3] >> doc
    peer1[1] >> doc
    validator[0] >> peer1[0]
    peer1[2] >> validator[2] >> db[0] >> dbase
    peer1[3] >> validator[2]
    peer1[3] >> validator[2]
