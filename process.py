import sys
import json
import Connectors
import Transformations
import AutoML
try:
    Adnan-1_DBFS = Connectors.DBFSConnector.fetch([], {}, "5e96eb44c4557e6540204311", spark, "{'url': '', 'file_type': 'Delimeted', 'dbfs_token': '', 'dbfs_domain': '', 'delimiter': ',', 'is_header': 'Use Header Line'}")

except Exception as ex:
    print(ex)
try:
    Adnan-1_AutoFE = Transformations.TransformationMain.run(["5e96eb44c4557e6540204311"], {"5e96eb44c4557e6540204311": Adnan-1_DBFS}, "5e96eb44c4557e6540204312", spark, json.dumps({"FE": []}))

except Exception as ex:
    print(ex)
try:
    AutoML.functionClassification(Adnan-1_AutoFE, [], "")

except Exception as ex:
    print(ex)
