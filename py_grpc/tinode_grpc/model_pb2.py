# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bmodel.proto\x12\x03pbx\"\x08\n\x06Unused\",\n\x0e\x44\x65\x66\x61ultAcsMode\x12\x0c\n\x04\x61uth\x18\x01 \x01(\t\x12\x0c\n\x04\x61non\x18\x02 \x01(\t\")\n\nAccessMode\x12\x0c\n\x04want\x18\x01 \x01(\t\x12\r\n\x05given\x18\x02 \x01(\t\"\'\n\x06SetSub\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0c\n\x04mode\x18\x02 \x01(\t\"\x99\x01\n\nClientCred\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x10\n\x08response\x18\x03 \x01(\t\x12+\n\x06params\x18\x04 \x03(\x0b\x32\x1b.pbx.ClientCred.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"e\n\x07SetDesc\x12(\n\x0b\x64\x65\x66\x61ult_acs\x18\x01 \x01(\x0b\x32\x13.pbx.DefaultAcsMode\x12\x0e\n\x06public\x18\x02 \x01(\x0c\x12\x0f\n\x07private\x18\x03 \x01(\x0c\x12\x0f\n\x07trusted\x18\x04 \x01(\x0c\"u\n\x07GetOpts\x12\x19\n\x11if_modified_since\x18\x01 \x01(\x03\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\r\n\x05topic\x18\x03 \x01(\t\x12\x10\n\x08since_id\x18\x04 \x01(\x05\x12\x11\n\tbefore_id\x18\x05 \x01(\x05\x12\r\n\x05limit\x18\x06 \x01(\x05\"k\n\x08GetQuery\x12\x0c\n\x04what\x18\x01 \x01(\t\x12\x1a\n\x04\x64\x65sc\x18\x02 \x01(\x0b\x32\x0c.pbx.GetOpts\x12\x19\n\x03sub\x18\x03 \x01(\x0b\x32\x0c.pbx.GetOpts\x12\x1a\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x0c.pbx.GetOpts\"m\n\x08SetQuery\x12\x1a\n\x04\x64\x65sc\x18\x01 \x01(\x0b\x32\x0c.pbx.SetDesc\x12\x18\n\x03sub\x18\x02 \x01(\x0b\x32\x0b.pbx.SetSub\x12\x0c\n\x04tags\x18\x03 \x03(\t\x12\x1d\n\x04\x63red\x18\x04 \x01(\x0b\x32\x0f.pbx.ClientCred\"#\n\x08SeqRange\x12\x0b\n\x03low\x18\x01 \x01(\x05\x12\n\n\x02hi\x18\x02 \x01(\x05\"~\n\x08\x43lientHi\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nuser_agent\x18\x02 \x01(\t\x12\x0b\n\x03ver\x18\x03 \x01(\t\x12\x11\n\tdevice_id\x18\x04 \x01(\t\x12\x0c\n\x04lang\x18\x05 \x01(\t\x12\x10\n\x08platform\x18\x06 \x01(\t\x12\x12\n\nbackground\x18\x07 \x01(\x08\"\x8a\x02\n\tClientAcc\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x0e\n\x06scheme\x18\x03 \x01(\t\x12\x0e\n\x06secret\x18\x04 \x01(\x0c\x12\r\n\x05login\x18\x05 \x01(\x08\x12\x0c\n\x04tags\x18\x06 \x03(\t\x12\x1a\n\x04\x64\x65sc\x18\x07 \x01(\x0b\x32\x0c.pbx.SetDesc\x12\x1d\n\x04\x63red\x18\x08 \x03(\x0b\x32\x0f.pbx.ClientCred\x12\r\n\x05token\x18\t \x01(\x0c\x12\r\n\x05state\x18\n \x01(\t\x12\"\n\nauth_level\x18\x0b \x01(\x0e\x32\x0e.pbx.AuthLevel\x12\x12\n\ntmp_scheme\x18\x0c \x01(\t\x12\x12\n\ntmp_secret\x18\r \x01(\x0c\"X\n\x0b\x43lientLogin\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06scheme\x18\x02 \x01(\t\x12\x0e\n\x06secret\x18\x03 \x01(\x0c\x12\x1d\n\x04\x63red\x18\x04 \x03(\x0b\x32\x0f.pbx.ClientCred\"j\n\tClientSub\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12 \n\tset_query\x18\x03 \x01(\x0b\x32\r.pbx.SetQuery\x12 \n\tget_query\x18\x04 \x01(\x0b\x32\r.pbx.GetQuery\"7\n\x0b\x43lientLeave\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\r\n\x05unsub\x18\x03 \x01(\x08\"\x9d\x01\n\tClientPub\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x0f\n\x07no_echo\x18\x03 \x01(\x08\x12&\n\x04head\x18\x04 \x03(\x0b\x32\x18.pbx.ClientPub.HeadEntry\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\x0c\x1a+\n\tHeadEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"D\n\tClientGet\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x1c\n\x05query\x18\x03 \x01(\x0b\x32\r.pbx.GetQuery\"D\n\tClientSet\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x1c\n\x05query\x18\x03 \x01(\x0b\x32\r.pbx.SetQuery\"\xe8\x01\n\tClientDel\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12!\n\x04what\x18\x03 \x01(\x0e\x32\x13.pbx.ClientDel.What\x12\x1e\n\x07\x64\x65l_seq\x18\x04 \x03(\x0b\x32\r.pbx.SeqRange\x12\x0f\n\x07user_id\x18\x05 \x01(\t\x12\x1d\n\x04\x63red\x18\x06 \x01(\x0b\x32\x0f.pbx.ClientCred\x12\x0c\n\x04hard\x18\x07 \x01(\x08\"?\n\x04What\x12\x06\n\x02X0\x10\x00\x12\x07\n\x03MSG\x10\x01\x12\t\n\x05TOPIC\x10\x02\x12\x07\n\x03SUB\x10\x03\x12\x08\n\x04USER\x10\x04\x12\x08\n\x04\x43RED\x10\x05\"\x88\x01\n\nClientNote\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x1b\n\x04what\x18\x02 \x01(\x0e\x32\r.pbx.InfoNote\x12\x0e\n\x06seq_id\x18\x03 \x01(\x05\x12\x0e\n\x06unread\x18\x04 \x01(\x05\x12\x1d\n\x05\x65vent\x18\x05 \x01(\x0e\x32\x0e.pbx.CallEvent\x12\x0f\n\x07payload\x18\x06 \x01(\x0c\"\\\n\x0b\x43lientExtra\x12\x13\n\x0b\x61ttachments\x18\x01 \x03(\t\x12\x14\n\x0con_behalf_of\x18\x02 \x01(\t\x12\"\n\nauth_level\x18\x03 \x01(\x0e\x32\x0e.pbx.AuthLevel\"\xf5\x02\n\tClientMsg\x12\x1b\n\x02hi\x18\x01 \x01(\x0b\x32\r.pbx.ClientHiH\x00\x12\x1d\n\x03\x61\x63\x63\x18\x02 \x01(\x0b\x32\x0e.pbx.ClientAccH\x00\x12!\n\x05login\x18\x03 \x01(\x0b\x32\x10.pbx.ClientLoginH\x00\x12\x1d\n\x03sub\x18\x04 \x01(\x0b\x32\x0e.pbx.ClientSubH\x00\x12!\n\x05leave\x18\x05 \x01(\x0b\x32\x10.pbx.ClientLeaveH\x00\x12\x1d\n\x03pub\x18\x06 \x01(\x0b\x32\x0e.pbx.ClientPubH\x00\x12\x1d\n\x03get\x18\x07 \x01(\x0b\x32\x0e.pbx.ClientGetH\x00\x12\x1d\n\x03set\x18\x08 \x01(\x0b\x32\x0e.pbx.ClientSetH\x00\x12\x1d\n\x03\x64\x65l\x18\t \x01(\x0b\x32\x0e.pbx.ClientDelH\x00\x12\x1f\n\x04note\x18\n \x01(\x0b\x32\x0f.pbx.ClientNoteH\x00\x12\x1f\n\x05\x65xtra\x18\r \x01(\x0b\x32\x10.pbx.ClientExtraB\t\n\x07Message\"9\n\nServerCred\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0c\n\x04\x64one\x18\x03 \x01(\x08\"\xf6\x02\n\tTopicDesc\x12\x12\n\ncreated_at\x18\x01 \x01(\x03\x12\x12\n\nupdated_at\x18\x02 \x01(\x03\x12\x12\n\ntouched_at\x18\x03 \x01(\x03\x12#\n\x06\x64\x65\x66\x61\x63s\x18\x04 \x01(\x0b\x32\x13.pbx.DefaultAcsMode\x12\x1c\n\x03\x61\x63s\x18\x05 \x01(\x0b\x32\x0f.pbx.AccessMode\x12\x0e\n\x06seq_id\x18\x06 \x01(\x05\x12\x0f\n\x07read_id\x18\x07 \x01(\x05\x12\x0f\n\x07recv_id\x18\x08 \x01(\x05\x12\x0e\n\x06\x64\x65l_id\x18\t \x01(\x05\x12\x0e\n\x06public\x18\n \x01(\x0c\x12\x0f\n\x07private\x18\x0b \x01(\x0c\x12\r\n\x05state\x18\x0c \x01(\t\x12\x10\n\x08state_at\x18\r \x01(\x03\x12\x0f\n\x07trusted\x18\x0e \x01(\x0c\x12\x0f\n\x07is_chan\x18\x11 \x01(\x08\x12\x0e\n\x06online\x18\x12 \x01(\x08\x12\x16\n\x0elast_seen_time\x18\x0f \x01(\x03\x12\x1c\n\x14last_seen_user_agent\x18\x10 \x01(\t\"\xbe\x02\n\x08TopicSub\x12\x12\n\nupdated_at\x18\x01 \x01(\x03\x12\x12\n\ndeleted_at\x18\x02 \x01(\x03\x12\x0e\n\x06online\x18\x03 \x01(\x08\x12\x1c\n\x03\x61\x63s\x18\x04 \x01(\x0b\x32\x0f.pbx.AccessMode\x12\x0f\n\x07read_id\x18\x05 \x01(\x05\x12\x0f\n\x07recv_id\x18\x06 \x01(\x05\x12\x0e\n\x06public\x18\x07 \x01(\x0c\x12\x0f\n\x07trusted\x18\x10 \x01(\x0c\x12\x0f\n\x07private\x18\x08 \x01(\x0c\x12\x0f\n\x07user_id\x18\t \x01(\t\x12\r\n\x05topic\x18\n \x01(\t\x12\x12\n\ntouched_at\x18\x0b \x01(\x03\x12\x0e\n\x06seq_id\x18\x0c \x01(\x05\x12\x0e\n\x06\x64\x65l_id\x18\r \x01(\x05\x12\x16\n\x0elast_seen_time\x18\x0e \x01(\x03\x12\x1c\n\x14last_seen_user_agent\x18\x0f \x01(\t\";\n\tDelValues\x12\x0e\n\x06\x64\x65l_id\x18\x01 \x01(\x05\x12\x1e\n\x07\x64\x65l_seq\x18\x02 \x03(\x0b\x32\r.pbx.SeqRange\"\x9f\x01\n\nServerCtrl\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\x05\x12\x0c\n\x04text\x18\x04 \x01(\t\x12+\n\x06params\x18\x05 \x03(\x0b\x32\x1b.pbx.ServerCtrl.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\xcf\x01\n\nServerData\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x14\n\x0c\x66rom_user_id\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x07 \x01(\x03\x12\x12\n\ndeleted_at\x18\x03 \x01(\x03\x12\x0e\n\x06seq_id\x18\x04 \x01(\x05\x12\'\n\x04head\x18\x05 \x03(\x0b\x32\x19.pbx.ServerData.HeadEntry\x12\x0f\n\x07\x63ontent\x18\x06 \x01(\x0c\x1a+\n\tHeadEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\xec\x02\n\nServerPres\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x0b\n\x03src\x18\x02 \x01(\t\x12\"\n\x04what\x18\x03 \x01(\x0e\x32\x14.pbx.ServerPres.What\x12\x12\n\nuser_agent\x18\x04 \x01(\t\x12\x0e\n\x06seq_id\x18\x05 \x01(\x05\x12\x0e\n\x06\x64\x65l_id\x18\x06 \x01(\x05\x12\x1e\n\x07\x64\x65l_seq\x18\x07 \x03(\x0b\x32\r.pbx.SeqRange\x12\x16\n\x0etarget_user_id\x18\x08 \x01(\t\x12\x15\n\ractor_user_id\x18\t \x01(\t\x12\x1c\n\x03\x61\x63s\x18\n \x01(\x0b\x32\x0f.pbx.AccessMode\"}\n\x04What\x12\x06\n\x02X3\x10\x00\x12\x06\n\x02ON\x10\x01\x12\x07\n\x03OFF\x10\x02\x12\x06\n\x02UA\x10\x03\x12\x07\n\x03UPD\x10\x04\x12\x08\n\x04GONE\x10\x05\x12\x07\n\x03\x41\x43S\x10\x06\x12\x08\n\x04TERM\x10\x07\x12\x07\n\x03MSG\x10\x08\x12\x08\n\x04READ\x10\t\x12\x08\n\x04RECV\x10\n\x12\x07\n\x03\x44\x45L\x10\x0b\x12\x08\n\x04TAGS\x10\x0c\"\xab\x01\n\nServerMeta\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x1c\n\x04\x64\x65sc\x18\x03 \x01(\x0b\x32\x0e.pbx.TopicDesc\x12\x1a\n\x03sub\x18\x04 \x03(\x0b\x32\r.pbx.TopicSub\x12\x1b\n\x03\x64\x65l\x18\x05 \x01(\x0b\x32\x0e.pbx.DelValues\x12\x0c\n\x04tags\x18\x06 \x03(\t\x12\x1d\n\x04\x63red\x18\x07 \x03(\x0b\x32\x0f.pbx.ServerCred\"\x9b\x01\n\nServerInfo\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x14\n\x0c\x66rom_user_id\x18\x02 \x01(\t\x12\x1b\n\x04what\x18\x03 \x01(\x0e\x32\r.pbx.InfoNote\x12\x0e\n\x06seq_id\x18\x04 \x01(\x05\x12\x0b\n\x03src\x18\x05 \x01(\t\x12\x1d\n\x05\x65vent\x18\x06 \x01(\x0e\x32\x0e.pbx.CallEvent\x12\x0f\n\x07payload\x18\x07 \x01(\x0c\"\xce\x01\n\tServerMsg\x12\x1f\n\x04\x63trl\x18\x01 \x01(\x0b\x32\x0f.pbx.ServerCtrlH\x00\x12\x1f\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x0f.pbx.ServerDataH\x00\x12\x1f\n\x04pres\x18\x03 \x01(\x0b\x32\x0f.pbx.ServerPresH\x00\x12\x1f\n\x04meta\x18\x04 \x01(\x0b\x32\x0f.pbx.ServerMetaH\x00\x12\x1f\n\x04info\x18\x05 \x01(\x0b\x32\x0f.pbx.ServerInfoH\x00\x12\x11\n\x05topic\x18\x06 \x01(\tB\x02\x18\x01\x42\t\n\x07Message\"j\n\nServerResp\x12\x1d\n\x06status\x18\x01 \x01(\x0e\x32\r.pbx.RespCode\x12\x1e\n\x06srvmsg\x18\x02 \x01(\x0b\x32\x0e.pbx.ServerMsg\x12\x1d\n\x05\x63lmsg\x18\x03 \x01(\x0b\x32\x0e.pbx.ClientMsg\"\xa0\x01\n\x07Session\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\"\n\nauth_level\x18\x03 \x01(\x0e\x32\x0e.pbx.AuthLevel\x12\x13\n\x0bremote_addr\x18\x04 \x01(\t\x12\x12\n\nuser_agent\x18\x05 \x01(\t\x12\x11\n\tdevice_id\x18\x06 \x01(\t\x12\x10\n\x08language\x18\x07 \x01(\t\"D\n\tClientReq\x12\x1b\n\x03msg\x18\x01 \x01(\x0b\x32\x0e.pbx.ClientMsg\x12\x1a\n\x04sess\x18\x02 \x01(\x0b\x32\x0c.pbx.Session\"-\n\x0bSearchQuery\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\r\n\x05query\x18\x02 \x01(\t\"Z\n\x0bSearchFound\x12\x1d\n\x06status\x18\x01 \x01(\x0e\x32\r.pbx.RespCode\x12\r\n\x05query\x18\x02 \x01(\t\x12\x1d\n\x06result\x18\x03 \x03(\x0b\x32\r.pbx.TopicSub\"S\n\nTopicEvent\x12\x19\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\t.pbx.Crud\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1c\n\x04\x64\x65sc\x18\x03 \x01(\x0b\x32\x0e.pbx.TopicDesc\"\x82\x01\n\x0c\x41\x63\x63ountEvent\x12\x19\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\t.pbx.Crud\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12(\n\x0b\x64\x65\x66\x61ult_acs\x18\x03 \x01(\x0b\x32\x13.pbx.DefaultAcsMode\x12\x0e\n\x06public\x18\x04 \x01(\x0c\x12\x0c\n\x04tags\x18\x08 \x03(\t\"\xb0\x01\n\x11SubscriptionEvent\x12\x19\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\t.pbx.Crud\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x0e\n\x06\x64\x65l_id\x18\x04 \x01(\x05\x12\x0f\n\x07read_id\x18\x05 \x01(\x05\x12\x0f\n\x07recv_id\x18\x06 \x01(\x05\x12\x1d\n\x04mode\x18\x07 \x01(\x0b\x32\x0f.pbx.AccessMode\x12\x0f\n\x07private\x18\x08 \x01(\x0c\"G\n\x0cMessageEvent\x12\x19\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\t.pbx.Crud\x12\x1c\n\x03msg\x18\x02 \x01(\x0b\x32\x0f.pbx.ServerData*3\n\tAuthLevel\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04\x41NON\x10\n\x12\x08\n\x04\x41UTH\x10\x14\x12\x08\n\x04ROOT\x10\x1e*8\n\x08InfoNote\x12\x06\n\x02X1\x10\x00\x12\x08\n\x04READ\x10\x01\x12\x08\n\x04RECV\x10\x02\x12\x06\n\x02KP\x10\x03\x12\x08\n\x04\x43\x41LL\x10\x04*o\n\tCallEvent\x12\x06\n\x02X2\x10\x00\x12\n\n\x06\x41\x43\x43\x45PT\x10\x01\x12\n\n\x06\x41NSWER\x10\x02\x12\x0b\n\x07HANG_UP\x10\x03\x12\x11\n\rICE_CANDIDATE\x10\x04\x12\n\n\x06INVITE\x10\x05\x12\t\n\x05OFFER\x10\x06\x12\x0b\n\x07RINGING\x10\x07*<\n\x08RespCode\x12\x0c\n\x08\x43ONTINUE\x10\x00\x12\x08\n\x04\x44ROP\x10\x01\x12\x0b\n\x07RESPOND\x10\x02\x12\x0b\n\x07REPLACE\x10\x03**\n\x04\x43rud\x12\n\n\x06\x43REATE\x10\x00\x12\n\n\x06UPDATE\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02\x32;\n\x04Node\x12\x33\n\x0bMessageLoop\x12\x0e.pbx.ClientMsg\x1a\x0e.pbx.ServerMsg\"\x00(\x01\x30\x01\x32\x9f\x02\n\x06Plugin\x12-\n\x08\x46ireHose\x12\x0e.pbx.ClientReq\x1a\x0f.pbx.ServerResp\"\x00\x12,\n\x04\x46ind\x12\x10.pbx.SearchQuery\x1a\x10.pbx.SearchFound\"\x00\x12+\n\x07\x41\x63\x63ount\x12\x11.pbx.AccountEvent\x1a\x0b.pbx.Unused\"\x00\x12\'\n\x05Topic\x12\x0f.pbx.TopicEvent\x1a\x0b.pbx.Unused\"\x00\x12\x35\n\x0cSubscription\x12\x16.pbx.SubscriptionEvent\x1a\x0b.pbx.Unused\"\x00\x12+\n\x07Message\x12\x11.pbx.MessageEvent\x1a\x0b.pbx.Unused\"\x00\x42\x1cZ\x1agithub.com/tinode/chat/pbxb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\032github.com/tinode/chat/pbx'
  _globals['_CLIENTCRED_PARAMSENTRY']._loaded_options = None
  _globals['_CLIENTCRED_PARAMSENTRY']._serialized_options = b'8\001'
  _globals['_CLIENTPUB_HEADENTRY']._loaded_options = None
  _globals['_CLIENTPUB_HEADENTRY']._serialized_options = b'8\001'
  _globals['_SERVERCTRL_PARAMSENTRY']._loaded_options = None
  _globals['_SERVERCTRL_PARAMSENTRY']._serialized_options = b'8\001'
  _globals['_SERVERDATA_HEADENTRY']._loaded_options = None
  _globals['_SERVERDATA_HEADENTRY']._serialized_options = b'8\001'
  _globals['_SERVERMSG'].fields_by_name['topic']._loaded_options = None
  _globals['_SERVERMSG'].fields_by_name['topic']._serialized_options = b'\030\001'
  _globals['_AUTHLEVEL']._serialized_start=5639
  _globals['_AUTHLEVEL']._serialized_end=5690
  _globals['_INFONOTE']._serialized_start=5692
  _globals['_INFONOTE']._serialized_end=5748
  _globals['_CALLEVENT']._serialized_start=5750
  _globals['_CALLEVENT']._serialized_end=5861
  _globals['_RESPCODE']._serialized_start=5863
  _globals['_RESPCODE']._serialized_end=5923
  _globals['_CRUD']._serialized_start=5925
  _globals['_CRUD']._serialized_end=5967
  _globals['_UNUSED']._serialized_start=20
  _globals['_UNUSED']._serialized_end=28
  _globals['_DEFAULTACSMODE']._serialized_start=30
  _globals['_DEFAULTACSMODE']._serialized_end=74
  _globals['_ACCESSMODE']._serialized_start=76
  _globals['_ACCESSMODE']._serialized_end=117
  _globals['_SETSUB']._serialized_start=119
  _globals['_SETSUB']._serialized_end=158
  _globals['_CLIENTCRED']._serialized_start=161
  _globals['_CLIENTCRED']._serialized_end=314
  _globals['_CLIENTCRED_PARAMSENTRY']._serialized_start=269
  _globals['_CLIENTCRED_PARAMSENTRY']._serialized_end=314
  _globals['_SETDESC']._serialized_start=316
  _globals['_SETDESC']._serialized_end=417
  _globals['_GETOPTS']._serialized_start=419
  _globals['_GETOPTS']._serialized_end=536
  _globals['_GETQUERY']._serialized_start=538
  _globals['_GETQUERY']._serialized_end=645
  _globals['_SETQUERY']._serialized_start=647
  _globals['_SETQUERY']._serialized_end=756
  _globals['_SEQRANGE']._serialized_start=758
  _globals['_SEQRANGE']._serialized_end=793
  _globals['_CLIENTHI']._serialized_start=795
  _globals['_CLIENTHI']._serialized_end=921
  _globals['_CLIENTACC']._serialized_start=924
  _globals['_CLIENTACC']._serialized_end=1190
  _globals['_CLIENTLOGIN']._serialized_start=1192
  _globals['_CLIENTLOGIN']._serialized_end=1280
  _globals['_CLIENTSUB']._serialized_start=1282
  _globals['_CLIENTSUB']._serialized_end=1388
  _globals['_CLIENTLEAVE']._serialized_start=1390
  _globals['_CLIENTLEAVE']._serialized_end=1445
  _globals['_CLIENTPUB']._serialized_start=1448
  _globals['_CLIENTPUB']._serialized_end=1605
  _globals['_CLIENTPUB_HEADENTRY']._serialized_start=1562
  _globals['_CLIENTPUB_HEADENTRY']._serialized_end=1605
  _globals['_CLIENTGET']._serialized_start=1607
  _globals['_CLIENTGET']._serialized_end=1675
  _globals['_CLIENTSET']._serialized_start=1677
  _globals['_CLIENTSET']._serialized_end=1745
  _globals['_CLIENTDEL']._serialized_start=1748
  _globals['_CLIENTDEL']._serialized_end=1980
  _globals['_CLIENTDEL_WHAT']._serialized_start=1917
  _globals['_CLIENTDEL_WHAT']._serialized_end=1980
  _globals['_CLIENTNOTE']._serialized_start=1983
  _globals['_CLIENTNOTE']._serialized_end=2119
  _globals['_CLIENTEXTRA']._serialized_start=2121
  _globals['_CLIENTEXTRA']._serialized_end=2213
  _globals['_CLIENTMSG']._serialized_start=2216
  _globals['_CLIENTMSG']._serialized_end=2589
  _globals['_SERVERCRED']._serialized_start=2591
  _globals['_SERVERCRED']._serialized_end=2648
  _globals['_TOPICDESC']._serialized_start=2651
  _globals['_TOPICDESC']._serialized_end=3025
  _globals['_TOPICSUB']._serialized_start=3028
  _globals['_TOPICSUB']._serialized_end=3346
  _globals['_DELVALUES']._serialized_start=3348
  _globals['_DELVALUES']._serialized_end=3407
  _globals['_SERVERCTRL']._serialized_start=3410
  _globals['_SERVERCTRL']._serialized_end=3569
  _globals['_SERVERCTRL_PARAMSENTRY']._serialized_start=269
  _globals['_SERVERCTRL_PARAMSENTRY']._serialized_end=314
  _globals['_SERVERDATA']._serialized_start=3572
  _globals['_SERVERDATA']._serialized_end=3779
  _globals['_SERVERDATA_HEADENTRY']._serialized_start=1562
  _globals['_SERVERDATA_HEADENTRY']._serialized_end=1605
  _globals['_SERVERPRES']._serialized_start=3782
  _globals['_SERVERPRES']._serialized_end=4146
  _globals['_SERVERPRES_WHAT']._serialized_start=4021
  _globals['_SERVERPRES_WHAT']._serialized_end=4146
  _globals['_SERVERMETA']._serialized_start=4149
  _globals['_SERVERMETA']._serialized_end=4320
  _globals['_SERVERINFO']._serialized_start=4323
  _globals['_SERVERINFO']._serialized_end=4478
  _globals['_SERVERMSG']._serialized_start=4481
  _globals['_SERVERMSG']._serialized_end=4687
  _globals['_SERVERRESP']._serialized_start=4689
  _globals['_SERVERRESP']._serialized_end=4795
  _globals['_SESSION']._serialized_start=4798
  _globals['_SESSION']._serialized_end=4958
  _globals['_CLIENTREQ']._serialized_start=4960
  _globals['_CLIENTREQ']._serialized_end=5028
  _globals['_SEARCHQUERY']._serialized_start=5030
  _globals['_SEARCHQUERY']._serialized_end=5075
  _globals['_SEARCHFOUND']._serialized_start=5077
  _globals['_SEARCHFOUND']._serialized_end=5167
  _globals['_TOPICEVENT']._serialized_start=5169
  _globals['_TOPICEVENT']._serialized_end=5252
  _globals['_ACCOUNTEVENT']._serialized_start=5255
  _globals['_ACCOUNTEVENT']._serialized_end=5385
  _globals['_SUBSCRIPTIONEVENT']._serialized_start=5388
  _globals['_SUBSCRIPTIONEVENT']._serialized_end=5564
  _globals['_MESSAGEEVENT']._serialized_start=5566
  _globals['_MESSAGEEVENT']._serialized_end=5637
  _globals['_NODE']._serialized_start=5969
  _globals['_NODE']._serialized_end=6028
  _globals['_PLUGIN']._serialized_start=6031
  _globals['_PLUGIN']._serialized_end=6318
# @@protoc_insertion_point(module_scope)
