/*
This  Uday's Data fix to make  entry into MTLSApplication cluster root for Buyer and S4 application in ALL DC's.
*/

var BaseSession = ariba.base.core.BaseSession;  
var Base = ariba.base.core.Base;
var newSession = new ariba.base.server.ObjectServerSession(
                ariba.base.server.BaseServer.baseServer(),
                BaseSession.SessionTypeDefault,
                ariba.base.fields.Realm.System);
            newSession.setPartition(ariba.base.core.Partition.None);
            Base.setSession(null);
            Base.setSession(newSession);
var str = "";
var errors = "";
var br = "<br>\n";

function execute (mapEntryValue)
{
    var mapEntry;
    try {
            str += "entered";
            newSession.transactionBegin();
            str += "\nentered2";
            mapEntry = new ariba.integration.core.MTLSApplication();
str += "\nentered3";
            mapEntry.setName(mapEntryValue);
str += "\nentered4";    
            mapEntry.save();
str += "\nentered5";
            str += "Inserted ApplicationName entry with key: " + mapEntryValue;
            newSession.transactionCommit();
    }
    catch (error) {
        errors = errors + br + "Exception: " + error;
    }
 return mapEntry;
}
execute(ariba.util.parameters.AppInfo.getRunningAppInfo().getType());
str + errors;
