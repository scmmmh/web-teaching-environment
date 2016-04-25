Search.setIndex({envversion:46,filenames:["administrator/configuration","administrator/deployment","administrator/index","administrator/installation","administrator/setup","administrator/updating","api/index","api/wte","api/wte_decorators","api/wte_doc","api/wte_helpers","api/wte_helpers_frontend","api/wte_models","api/wte_scripts","api/wte_scripts_configuration","api/wte_scripts_database","api/wte_scripts_main","api/wte_scripts_timed_tasks","api/wte_text_formatter","api/wte_text_formatter_docutils_ext","api/wte_util","api/wte_views","api/wte_views_admin","api/wte_views_asset","api/wte_views_part","api/wte_views_timed_tasks","api/wte_views_user","api/wte_views_user_role","index","user/index","user/learner/html_editor_part","user/learner/index","user/learner/module","user/learner/modules","user/learner/my_modules","user/learner/take_module","user/learner/text_part","user/teacher/asset/delete","user/teacher/asset/edit","user/teacher/asset/index","user/teacher/asset/new","user/teacher/download","user/teacher/editor/asset","user/teacher/editor/crossref","user/teacher/editor/index","user/teacher/editor/rst-primer","user/teacher/editor/sourcecode","user/teacher/editor/video","user/teacher/import_export","user/teacher/index","user/teacher/module/access_settings","user/teacher/module/delete","user/teacher/module/edit","user/teacher/module/index","user/teacher/module/new","user/teacher/module/users","user/teacher/page/delete","user/teacher/page/edit","user/teacher/page/index","user/teacher/page/new","user/teacher/part/delete","user/teacher/part/edit","user/teacher/part/index","user/teacher/part/new","user/teacher/status","user/teacher/timed_actions","user/user/forgotten_password","user/user/index","user/user/login","user/user/profile","user/user/register"],objects:{"":{wte:[7,0,0,"-"]},"wte.decorators":{current_user:[8,3,1,""],request_from_args:[8,3,1,""],require_logged_in:[8,3,1,""],require_method:[8,3,1,""]},"wte.doc":{button_role:[9,3,1,""],link_role:[9,3,1,""],setup:[9,3,1,""]},"wte.helpers":{frontend:[11,0,0,"-"],version:[10,3,1,""]},"wte.helpers.frontend":{MenuBuilder:[11,1,1,""],codemirror_options:[11,3,1,""],codemirror_scripts:[11,3,1,""],confirm_action:[11,3,1,""],confirm_delete:[11,3,1,""],html_id:[11,3,1,""],natural_list:[11,3,1,""],readable_timedelta:[11,3,1,""],set_list:[11,3,1,""],template_for_part:[11,3,1,""]},"wte.helpers.frontend.MenuBuilder":{generate:[11,2,1,""],group:[11,2,1,""],menu:[11,2,1,""]},"wte.models":{Asset:[12,1,1,""],DBUpgradeException:[12,6,1,""],DB_VERSION:[12,5,1,""],Part:[12,1,1,""],Permission:[12,1,1,""],PermissionGroup:[12,1,1,""],TimedTask:[12,1,1,""],User:[12,1,1,""],UserPartProgress:[12,1,1,""],UserPartRole:[12,1,1,""],check_database_version:[12,3,1,""],groups_permissions:[12,5,1,""],parts_assets:[12,5,1,""],progress_assets:[12,5,1,""],users_groups:[12,5,1,""],users_permissions:[12,5,1,""]},"wte.models.Asset":{menu:[12,2,1,""]},"wte.models.Part":{allow:[12,2,1,""],available_children:[12,4,1,""],has_role:[12,2,1,""],menu:[12,2,1,""],next:[12,4,1,""],prev:[12,4,1,""],root:[12,2,1,""],summary:[12,4,1,""]},"wte.models.TimedTask":{delta:[12,4,1,""],menu:[12,2,1,""],options:[12,4,1,""]},"wte.models.User":{allow:[12,2,1,""],has_permission:[12,2,1,""],new_password:[12,2,1,""],new_salt:[12,2,1,""],password_matches:[12,2,1,""],random_password:[12,2,1,""]},"wte.models.UserPartProgress":{allow:[12,2,1,""]},"wte.scripts":{configuration:[14,0,0,"-"],database:[15,0,0,"-"],main:[16,0,0,"-"],timed_tasks:[17,0,0,"-"]},"wte.scripts.configuration":{generate_config:[14,3,1,""],generate_custom_styling:[14,3,1,""],init:[14,3,1,""]},"wte.scripts.database":{init:[15,3,1,""],initialise_database:[15,3,1,""]},"wte.scripts.main":{get_user_parameter:[16,3,1,""],main:[16,3,1,""]},"wte.scripts.timed_tasks":{init:[17,3,1,""],run_change_status:[17,3,1,""],run_timed_tasks:[17,3,1,""]},"wte.text_formatter":{compile_rst:[18,3,1,""],docutils_ext:[19,0,0,"-"],init:[18,3,1,""]},"wte.text_formatter.docutils_ext":{HtmlTitleFormatter:[19,1,1,""],Pygments:[19,1,1,""],YouTube:[19,1,1,""],and_:[19,3,1,""],asset_ref_role:[19,3,1,""],crossref_role:[19,3,1,""],flag_bool_option:[19,3,1,""],init:[19,3,1,""],inline_css_role:[19,3,1,""],inline_pygments_role:[19,3,1,""]},"wte.util":{CSRFSchema:[20,1,1,""],CSRFValidator:[20,1,1,""],DateValidator:[20,1,1,""],DynamicSchema:[20,1,1,""],State:[20,1,1,""],TimeValidator:[20,1,1,""],convert_type:[20,3,1,""],get_config_setting:[20,3,1,""],ordered_counted_set:[20,3,1,""],paginate:[20,3,1,""],send_email:[20,3,1,""],timing_tween_factory:[20,3,1,""],unauthorised_redirect:[20,3,1,""],version:[20,3,1,""]},"wte.views":{admin:[22,0,0,"-"],asset:[23,0,0,"-"],help_page:[21,3,1,""],init:[21,3,1,""],notfound_404:[21,3,1,""],part:[24,0,0,"-"],root:[21,3,1,""],servererror_500:[21,3,1,""],timed_tasks:[25,0,0,"-"],user:[26,0,0,"-"],user_role:[27,0,0,"-"]},"wte.views.admin":{admin:[22,3,1,""],content_admin:[22,3,1,""],content_regenerate:[22,3,1,""],init:[22,3,1,""]},"wte.views.asset":{"delete":[23,3,1,""],"new":[23,3,1,""],EditAssetSchema:[23,1,1,""],NewAssetSchema:[23,1,1,""],edit:[23,3,1,""],init:[23,3,1,""],save_file:[23,3,1,""],search:[23,3,1,""],view_asset:[23,3,1,""],view_file:[23,3,1,""]},"wte.views.asset.EditAssetSchema":{content:[23,4,1,""],data:[23,4,1,""],filename:[23,4,1,""],mimetype:[23,4,1,""],mimetype_other:[23,4,1,""]},"wte.views.asset.NewAssetSchema":{data:[23,4,1,""],filename:[23,4,1,""]},"wte.views.part":{"delete":[24,3,1,""],"export":[24,3,1,""],"new":[24,3,1,""],ChangeStatusSchema:[24,1,1,""],EditPartSchema:[24,1,1,""],ImportPartConverter:[24,1,1,""],ImportPartSchema:[24,1,1,""],NewPartSchema:[24,1,1,""],RegisterSettingsSchema:[24,1,1,""],ResetFilesSchema:[24,1,1,""],change_status:[24,3,1,""],create_part_crumbs:[24,3,1,""],crossref_replace:[24,3,1,""],deregister:[24,3,1,""],download:[24,3,1,""],download_part_progress:[24,3,1,""],edit:[24,3,1,""],edit_register_settings:[24,3,1,""],get_all_parts:[24,3,1,""],get_user_part_progress:[24,3,1,""],import_file:[24,3,1,""],init:[24,3,1,""],list_parts:[24,3,1,""],preview:[24,3,1,""],register:[24,3,1,""],reset_files:[24,3,1,""],search:[24,3,1,""],view_part:[24,3,1,""]},"wte.views.part.ChangeStatusSchema":{return_to:[24,4,1,""],status:[24,4,1,""]},"wte.views.part.EditPartSchema":{child_part_id:[24,4,1,""],content:[24,4,1,""],display_mode:[24,4,1,""],label:[24,4,1,""],status:[24,4,1,""],template_id:[24,4,1,""],title:[24,4,1,""]},"wte.views.part.ImportPartSchema":{file:[24,4,1,""],parent_id:[24,4,1,""]},"wte.views.part.NewPartSchema":{display_mode:[24,4,1,""],label:[24,4,1,""],order:[24,4,1,""],parent_id:[24,4,1,""],status:[24,4,1,""],title:[24,4,1,""]},"wte.views.part.RegisterSettingsSchema":{email_domains:[24,4,1,""],password:[24,4,1,""],require:[24,4,1,""]},"wte.views.part.ResetFilesSchema":{filename:[24,4,1,""]},"wte.views.timed_tasks":{EditTimedTaskSchema:[25,1,1,""],NewTimedTaskSchema:[25,1,1,""],delete_part_task:[25,3,1,""],edit_part_task:[25,3,1,""],init:[25,3,1,""],new_part_task:[25,3,1,""],view_part_tasks:[25,3,1,""]},"wte.views.timed_tasks.EditTimedTaskSchema":{date:[25,4,1,""],time:[25,4,1,""]},"wte.views.timed_tasks.NewTimedTaskSchema":{name:[25,4,1,""]},"wte.views.user":{"delete":[26,3,1,""],ActionSchema:[26,1,1,""],EditSchema:[26,1,1,""],EmailDomainValidator:[26,1,1,""],ForgottenPasswordSchema:[26,1,1,""],LoginSchema:[26,1,1,""],PasswordValidator:[26,1,1,""],RegisterSchema:[26,1,1,""],UniqueEmailValidator:[26,1,1,""],action:[26,3,1,""],confirm:[26,3,1,""],create_user_crumbs:[26,3,1,""],edit:[26,3,1,""],forgotten_password:[26,3,1,""],init:[26,3,1,""],login:[26,3,1,""],logout:[26,3,1,""],permissions:[26,3,1,""],process_confirmation:[26,3,1,""],process_forgotten_password:[26,3,1,""],register:[26,3,1,""],users:[26,3,1,""],view:[26,3,1,""]},"wte.views.user.ActionSchema":{action:[26,4,1,""],confirm:[26,4,1,""],q:[26,4,1,""],start:[26,4,1,""],status:[26,4,1,""]},"wte.views.user.EditSchema":{email:[26,4,1,""],name:[26,4,1,""],password:[26,4,1,""]},"wte.views.user.ForgottenPasswordSchema":{email:[26,4,1,""]},"wte.views.user.LoginSchema":{email:[26,4,1,""],password:[26,4,1,""],return_to:[26,4,1,""]},"wte.views.user.RegisterSchema":{email:[26,4,1,""],email_confirm:[26,4,1,""],name:[26,4,1,""],return_to:[26,4,1,""]},"wte.views.user_role":{ActionSchema:[27,1,1,""],AddUserSchema:[27,1,1,""],ChangeRoleSchema:[27,1,1,""],action:[27,3,1,""],add:[27,3,1,""],init:[27,3,1,""],update:[27,3,1,""],users:[27,3,1,""]},"wte.views.user_role.ActionSchema":{action:[27,4,1,""],role_id:[27,4,1,""]},"wte.views.user_role.AddUserSchema":{q:[27,4,1,""],role:[27,4,1,""],start:[27,4,1,""],user_id:[27,4,1,""]},"wte.views.user_role.ChangeRoleSchema":{action:[27,4,1,""],q:[27,4,1,""],role:[27,4,1,""],role_id:[27,4,1,""],start:[27,4,1,""]},wte:{decorators:[8,0,0,"-"],doc:[9,0,0,"-"],helpers:[10,0,0,"-"],main:[7,3,1,""],models:[12,0,0,"-"],scripts:[13,0,0,"-"],text_formatter:[18,0,0,"-"],util:[20,0,0,"-"],views:[21,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","function","Python function"],"4":["py","attribute","Python attribute"],"5":["py","data","Python data"],"6":["py","exception","Python exception"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:function","4":"py:attribute","5":"py:data","6":"py:exception"},terms:{"01d":1,"02d":1,"465d42577343":12,"__file__":1,"_option":12,"abstract":12,"boolean":[11,20],"break":[20,45],"case":[0,5,12,19,25,27,68,70],"class":[11,12,19,20,23,24,25,26,27],"export":[],"final":[5,11,24,55],"function":0,"import":[],"int":20,"long":[30,45],"new":[5,11],"return":[7,8,10,11,12,16,18,19,20,24],"static":20,"switch":30,"true":[1,12,19,20],"try":[30,45,48],"while":[13,24,30,39],abil:39,abl:[26,49],abov:1,acccess:50,accept:4,access:0,access_right:[12,24],account:[0,66,67],accuraci:65,across:49,act:12,action:[],actionschema:[26,27],activ:[1,5,50,55],actual:[1,5,12,13,16,18,24,30,46,49,55,58,69,70],adapt:[0,1],add:[0,11,22],addit:[0,4,11,19,24,25,53,55],addition:[12,30,36,52,61],address:[0,12,20,26,50,55,66,68,69,70],addsitedir:1,adduserschema:27,adjust:19,admin:4,adminstr:13,affect:[50,55],after:[0,3,4,5,17,26,30,35,45,46,50,55,58,59,65,66,69,70],again:[48,55],against:[19,20,26],aid:23,aim:[2,29,31],alchemi:4,alemb:12,all:[0,4,11,13,17,18,19,20,21,22,23,24,26,30,34,35,37,38,41,42,43,45,50,51,52,54,55,60,61,64,66],allow:[0,1,5,8,12,14,19,24,26,30,48,50,52,57,59,61,63,65],alreadi:[26,50,55],also:[3,4,5,19,23,24,26,34,40,42,44,48,50,51,53,55,56,58,60,62,64,69],altern:[23,30,42,55,59],alwai:[20,50,52,54,55,57,61,63],amount:[1,45,49],ancestor:23,and_:19,angl:[42,43],ani:[0,1,4,5,12,17,19,20,23,24,30,38,39,40,41,42,45,48,50,51,52,55,56,57,60,61,64,65,68,69,70],anonym:8,anoth:[24,42,43,48,59],anyth:[45,49,62],app:[0,9],appear:[20,44,55,69],append:1,appli:[26,27,48,55],appropri:[16,20,21,26],arbitrari:[0,19,57,59,61,63],archiv:[24,53,64],area:[30,69],arg:[8,14,15,17,20,23,24,25,26,27],argument:19,argumentpars:[14,15,16,17],aris:5,arrang:[52,61],ask:[4,30,35,37,51,55,56,60,65,69],aspect:69,asset:[],asset_id:12,asset_ref_rol:19,assign:[19,57,59,61,63],associ:24,assur:45,asterisk:45,attach:[12,56],attack:[12,20],attempt:20,attr:11,attribut:[8,11,12,20,22,26,38,52,54,57,61],augment:44,auth:10,authent:0,author:[0,19],authoris:26,autom:1,automat:[0,5,17,19,20,30,40,42,45,47,65],avail:[0,4,22],available_children:12,back:[5,23,24,30,35,55,68,69],backend:[],backtick:45,backup:[5,48],baddicttyp:[20,23,24,25,26,27],badtyp:[20,23,24,25,26,27],base:[0,14,20,26,50],basic:[36,44,45,49],beaker:0,becaus:45,becom:30,been:[0,1,3,11,12,26,30,39,55,64,66],befor:[1,5,12,26,45,58,59],behavior:19,behind:45,belong:[12,23,24,25,26,50,64],below:[19,42,52,61,65],between:[12,19,24,26,30,36,45,48],bin:1,bind:12,bitbucket:[3,5],blank:[20,46,69],block:[],block_text:19,blue:70,bodi:[18,20,46],bold:45,bool:[11,12],both:[4,29,45,53,58,62,68,70],bottom:[30,35,36,37,38,55],box:[11,42,43,50,55],bracket:[42,43],breadcrumb:[24,26],brief:33,brows:[38,40,48],browser:[30,40,70],brute:12,bsd:19,build:16,built:0,bullet:45,button:[9,11,35,38,40,42,43,48,50,52,54,55,57,59,61,63,65,66,68,69,70],button_rol:9,cach:20,call:[11,12,16,21],can:[0,1,3,4,5,10,12,19,24,26,30,32,33,34,36,38,39,40,41,42,43,44,45,46,48,49,50,52,53,54,55,57,58,59,61,62,63,64,65,68,69,70],cancel:[11,48],cannot:[0,24,30,37,45,51,55,56,60,65,66,69,70],capitalis:20,cell:45,centr:[44,52,57,61],chang:[0,4],change_rol:27,change_statu:24,changeroleschema:27,changestatusschema:24,charact:[12,45],chdir:1,check:[8,12,20,24,26,65,66,70],check_database_vers:12,checkbox:[50,55],child:[12,24],child_part_id:24,children:[12,24],chunk:45,classif:[12,57,59,61,63],claus:19,clear:26,cleartext:12,click:[30,32,33,34,35,38,40,42,43,48,50,52,54,55,57,59,61,63,64,65,66,68,69,70],close:[1,45],code:[0,19,30,46,49],codemirror:[0,11,14],codemirror_opt:11,codemirror_script:11,column:[12,45,52,57,61],com:[0,4],combin:[19,30,49,55],come:[30,46],comfort:45,comma:[0,20,50],command:[0,1,3,5,14,15,16,17],commandlin:4,commun:12,compar:12,compil:[12,18],compile_rst:[18,19],compiled_cont:[12,22],complet:[3,4,16,17,24],complex:45,compon:0,compound:19,comput:40,conf:1,config:[1,4,14,21,22,23,24,25,26,27],confirm:[11,26,30,35,37,51,55,56,60,65,69,70],confirm_act:11,confirm_delet:11,conjunct:19,consist:[0,12,30,32,44,45,49,52,57,61,63],construct:[7,12],constructor:[20,25],consult:[0,1,10,45],contain:[8,9,11,12,13,16,18,19,21,24,30,38,41,46,53,55,58,61],content:22,content_admin:22,content_offset:19,content_regener:22,continu:[4,50,64],convers:[19,20],convert:[11,20,24],convert_typ:20,cooki:[0,3],copi:[19,47,48,70],copyright:19,core:[],corner:[30,34,46,55,68,69,70],correct:[0,11,23,24,43,45],correctli:[0,48],correspond:11,count:[11,20],counter:12,cover:[2,29,32],creat:[0,4,11],create_part_crumb:24,create_user_crumb:26,creation:16,criterion:55,cron:1,cross:[19,20,24,43,44,48],crossref:[19,43],crossref_replac:24,crossref_rol:19,crumb:[24,26],csrf:20,csrfschema:20,csrfvalid:20,css:[14,19,30,61,63],current:[8,10,11,12,19,20,23,24,26,32,42,43,59,61,63,65,69],current_id:12,current_us:8,cursor:[24,42,43],custom:[0,14,43],customis:14,data:[1,12,23,24,26,38],date:[20,25,65],datetim:[11,12,20],datevalid:20,db_version:12,dbsession:[24,26],dbupgradeexcept:12,ddd:25,deal:27,debug:0,debug_author:0,debug_notfound:0,debug_routematch:0,debug_templ:0,decor:[],decorator:[],default_config:14,default_locale_nam:0,defin:[20,22,23,24,25,26,27,53,55,61,63,64],definit:45,delet:11,delete_part_task:25,delta:[11,12],demo:0,demonstr:45,depend:[1,5,12,20,24,26,30,48,65],deploy:0,deregist:24,deriv:[12,20],design:0,desir:1,detail:[0,4,10,19,33,35,39,44,45,49,52,53,57,58,61,62],detect:20,determin:12,develop:0,dialog:11,dict:[11,12,19,20,23,24,25,26,27],differ:[19,24,32,45,61,63],direct:[19,46,47],directli:[12,45,46],directori:[0,1],dirnam:1,disallow:26,displai:[],display_mod:[12,24],display_nam:12,dissallow:26,distinct:45,distinguish:[12,26,39,45],divid:53,dlitz:[],doc:0,document:0,docutil:[],docutils_ext:[],doe:[3,12,16,20,24,26],doesn:45,domain:0,don:[4,38,48,52,57,61,69],done:[4,69],doubl:45,down:[30,34,36,55],download:5,download_part_progress:24,drag:[40,42,52,61],draw:45,drop:[4,30,34,36,55],dropdown:[59,63],dure:5,dynam:20,dynamicschema:20,each:[19,20,21,30,32,33,34,36,45,49,53,55,57,58,59,61,62,63],easi:49,easier:[12,43],easiest:45,easili:49,edit:[],edit_part_task:25,edit_register_set:24,editassetschema:23,editor:0,editpartschema:24,editschema:26,edittimedtaskschema:25,effect:19,egg:0,either:[3,4,12,20,23,40,42,45,54,55,68,69,70],element:[19,49,53],els:[49,62],email:[0,12,24,26],email_confirm:26,email_domain:[24,26],emaildomainvalid:26,emb:[19,47],embedded:19,empti:[11,20,23,24,25,26,27,42,45,46],enabl:[0,3,11,19,49],encrypt:0,encrypt_kei:0,end:[24,43,45],engin:0,enrol:19,ensur:[0,1,12,45,48],enter:[20,23,24,25,26,27,40,50,66,68,69,70],entir:49,entri:0,enumer:[45,46],error:[0,20,21,27,45,68],essenti:65,ever:17,everi:1,everyth:0,exact:42,exactli:[30,45],exampl:[4,19,42,45,46],except:[12,19,20],execut:[1,12],exercis:[12,24,32,62],exist:[4,24,25,26,66],expect:[1,20,23,24,25,26,27,65],experi:[0,1,4],express:19,extens:[18,19],extern:[24,48],factori:20,fail:[17,20,45],fals:[0,11,12,19],famou:45,fancyvalid:20,faster:20,featur:3,few:[30,66],fid:23,field:[20,23,24,25,26,27,40,66,68,69],fieldstorag:24,figur:45,file:[0,4,11],fileconfig:1,filenam:[4,12,19,23,24,30,38,40,42,46],filter:[],final_separ:11,find:[0,12,24,30,33,39,43,44,46,49,53,58,62],first:[1,4,5,8,12,42,45,50,70],flag_bool_opt:19,flash:20,flexibl:49,focu:24,folder:[66,70],follow:[0,1,3,4,5,10,12,21,26,30,38,42,43,45,46,47,49,53,58,59,62,63,64,65,68,69,70],font:45,footer:18,forc:12,foreignkei:12,forgeri:20,forgotten:[],forgotten_password:26,forgottenpasswordschema:26,form:[10,25,26],format:[0,18,19,20,25,44,45],formatt:19,formencod:20,forward:30,foundat:0,four:63,fragment:19,free:49,frequenc:20,frequent:[1,65],from:[0,1,3,4,5,8,12,14,19,20,24,30,34,38,40,42,45,46,47,48,55,59,63,69],front:1,frontend:[],fulfil:50,full:[0,11,32,33,46,52,57,61,64],funcation:44,further:[1,4,39,40,49,53,58,62,64],futur:12,gener:0,generate_config:14,generate_custom_styl:14,get:[12,19,20,24,45],get_all_part:24,get_app:1,get_config_set:20,get_user_paramet:16,get_user_part_progress:24,give:[45,55],given:[8,11,12,17,18,20,24,25,26,42,65],global_config:7,goe:[19,45,50],gori:19,grant:[12,50],greater:1,green:30,group:[1,11,12,62],groups_permiss:12,half:30,hand:[30,44,61,63],handler:[],harder:0,has_part:11,has_permiss:12,has_rol:12,hash:12,have:[0,1,3,5,12,17,19,20,23,24,25,26,27,30,42,45,46,50,55,61,63,64,66,68,69,70],head:[45,46],header:[18,45],help:[11,21,45],help_pag:21,helper:[],here:[0,19,24,39,42,43,44,46,49,52,53,57,58,61,62],high:53,highli:49,highlight:[0,11],host:0,hover:51,how:[0,1,5,46,48,61,63,65],howev:[50,55],href:11,html:[0,11],html_id:11,htmlformatt:19,htmltitleformatt:19,http:[0,3,5,19,45,47],http_port:1,human:11,icon:[11,30,34,37,38,40,41,48,50,51,52,53,54,56,57,58,59,60,61,62,63,64,65],id_map:24,idea:45,identifi:[12,17,24,43,69,70],imag:[19,39,42,49],immedi:[40,42,45,65,69],implement:[16,19,21],implicit:19,import_fil:24,importpartconvert:24,importpartschema:24,inact:30,includ:[0,4,11],include_mod:11,inclus:[42,46,49],incorrect:68,indent:[45,46],independ:17,index:[20,24,28,46],indic:[],individu:[12,17],inform:[0,26,33,35],ini:[0,1,4],init:[14,15,16,17,18,19,21,22,23,24,25,26,27],initi:[4,15,19,24,30,54,63],initialis:[],initialise_databas:15,inlin:[9,19],inline_css_rol:19,inline_pygments_rol:19,input:[16,20,23,24,25,26,27],insert:[8,24,40,42],instal:[],instanc:[1,12,17,24],instanti:24,instantli:[61,63],instead:[0,19,45],instruct:[1,18,29],integ:[12,20],integr:39,intend:3,interact:[30,40],interest:35,interfac:[27,30,49,50,54,59,63],intern:24,intersect:45,introduct:[],invalid:20,invalid_csrf_token:20,invalid_format:20,invalidpart:24,invalidstructur:24,invok:19,issu:5,ital:45,item:[1,11,20,30,34,37,38,40,41,45,48,50,51,52,56,57,59,60,61,63,64,65],itself:[0,12,44,64,69],javascript:[30,61,63],join:[11,19],jpg:42,jqueri:11,json:[11,12],jump:[30,36],just:[45,55],kei:[0,17,20],kind:[12,39],know:[4,45,50],kwarg:[12,19,20,25],label:[11,12,24,53,57,58,59,61,62,63],laid:30,land:[68,70],languag:[19,46],language_nam:19,larg:49,last:[0,11],later:[4,30,48,52,54,57,61,63],latest:[3,5],layout:45,learner:[31,39,44,49,50,51,52,53,54,57,60,61,63],least:[12,46],leav:[30,42,69],lectur:[32,62],left:[30,42,43,44,45,55,61,63],length:[12,45],level:[11,26,45,53],lib:1,librari:[0,3,5,46],licens:19,like:[19,20,23,24,25,26,27,30,45,61,63],limit:[0,12,50,62],line:[16,19,20,45,46],lineno:[19,46],link:[9,11,12,19,26,27,30,33,34,36,39,40,42,43,45,54,55,59,68,70],link_rol:9,list:[0,11,33],list_part:24,listen:[0,1],live:44,load:[0,1,11,19,27,30],local:[0,48],locat:1,lock:0,lock_dir:0,logging_config:1,logic:62,login:66,login_limit:12,loginschema:26,logout:26,look:[19,30,42,43,45,61,63],lost:11,lower:12,made:[12,30,65,69],mai:[12,50],main:[0,11],mainli:0,maintain:48,major:21,make:[4,5,30,49,50,53,58,62,64,69],malici:20,manag:0,mani:1,manipul:0,manual:[30,43,55],map:24,marker:[45,48],match:[12,23,24,26,42,43,50],matchobject:24,materi:[],matter:45,maximum:1,mean:[26,30],menu:[11,12,30,34,50,51,53,56,58,59,60,62,63,69],menubar:11,menubuild:11,messag:[11,20,23,24,25,26,27,66,68],metadata:12,method:[8,19],mhall:[3,5],mid:24,might:[20,30],migrat:3,mimetyp:[11,12,23],mimetype_oth:23,minut:[1,65,66],miss:[20,23,24,25,26,27],missingvalu:[20,23,24,25,26,27],mode:[11,12,24,39,61,63],model:[],modif:30,modifi:[24,46,55],modul:11,more:[0,1,11,12,30,32,44,45,50,55],most:[0,45],mous:[34,37,38,40,41,48,50,51,52,54,56,57,59,60,61,63,64,65,69],move:[3,30,34,37,38,40,41,48,50,52,54,56,57,59,60,61,63,64,65,69],multipl:[],must:[0,3,11,12,19,20,23,24,25,26,27,33,45,46,50,59,63,70],mysql:3,name:[0,12,19,20,21,22,23,24,25,26,27,34,42,46,55,69,70],natural_list:11,navig:[20,36,64,68,70],necessari:[9,11,26,40,42],need:[1,3,4,19,30,34,45,50,55,68,70],nest:45,net:0,new_part_task:25,new_password:12,new_salt:12,new_sys_path:1,new_typ:23,newassetschema:23,newli:68,newpartschema:24,newtimedtaskschema:25,next:[4,5,12,30,36,45,55],noconfirm:26,node_id:9,nologin:26,none:[11,12,18,19,20,23,24,25,26,27],nonetyp:[20,23,24,25,26,27],nopart:24,normal:[19,30],note:[19,42],notexpect:[20,23,24,25,26,27],notfound_404:21,noth:[0,26],notzip:24,now:12,nullabl:12,number:[0,1,10,12,17,19,20,43,46,49,53,62],numproc:1,obj_typ:11,object:[8,11,20],observ:45,offlin:[24,30,34,41],onc:[1,20],onli:[0,3,17,18,19,20,23,24,25,26,27,39,48,50,55,61,63,64,65],open:[30,40,45,48,64],oper:19,option:[0,4,11],or_:19,order:[11,12,19,20,24,46,52,61],ordered_counted_set:[11,20],org:[0,3,5,45],organis:33,origin:1,other:[],otherwis:[1,8,12,17,19,26],out:[26,30,45,69],outdat:12,over:[34,37,38,40,41,45,48,50,51,52,54,56,57,59,60,61,63,64,65,69],overrid:[0,42],overview:[53,57,59,61,62],overwrit:40,own:30,owner:[55,64],packag:[1,3,13,21],pad:45,page:[11,33],pagin:[20,27],pair:[20,45],paragraph:45,parallel:1,paramet:[4,8,11,12,16,18,19,20,23,24,25,26,27,65],parent:[12,24,45],parent_id:[12,24],parenthes:19,parser:16,part:[11,22],part_id:[12,19],part_typ:24,partial:11,parts_asset:12,pass:[0,8,20,25,46,55],password:[0,4],password_match:12,passwordvalid:26,past:[1,17,65],paster:1,path:[1,11],pattern:[21,22,23,24,25,26,27],pdf:42,per:20,perform:[5,12],perman:55,permiss:[12,15,23,24,26],permission_group:12,permission_group_id:12,permission_groups_permiss:12,permission_id:12,permissiongroup:[12,15,26],pid:[23,24,25,27],piec:45,pip:[3,5],place:[45,62],plai:12,pleas:[1,20,23,24,25,26,27,69,70],plugin:11,point:[0,24,30,42,43,47,52,54],port:[0,1],posit:[12,24,42,43],possibl:[0,1,17],post:26,postgresql:3,postlink:11,practic:30,preced:19,preceed:45,precis:1,prefix:45,prepar:[],prev:12,prev_sys_path:1,preview:[24,44],previou:[4,12,30,36],previous:[5,70],primary_kei:12,probabl:1,process:[0,1,9,16,26,70],process_confirm:26,process_forgotten_password:26,process_nam:1,process_num:1,produc:19,product:[0,1,4],profil:67,program:[1,70],program_nam:1,progress:[12,24],progress_asset:12,progress_id:12,project:69,prompt:16,provid:[0,1,3,4,7,11,12,13,14,15,16,17,19,20,23,24,25,26,27,39,42,44,46,49,59,63,68,70],pserv:1,pseudo:12,psycopg2:3,ptid:23,publicli:33,punctiat:45,pure:12,put:[5,43,45],pycrypto:3,pycryptopp:3,pygment:[0,14,19,46],pyramid_debugtoolbar:0,pyramid_tm:0,python2:1,python:[0,1,3,19,20],pywebtool:10,queri:[20,26,27],query_param:20,quick:45,quickli:[30,36],quot:45,r_type:[8,11,12,20],random:[12,17,26],random_password:12,randomli:0,rang:32,rawtext:[9,19],readabl:11,readable_timedelta:11,readi:[4,5,17],receiv:[26,66,70],recipi:20,recommend:[3,70],recurs:24,red:30,redirect:[8,20,26,27],redirect_to:20,refer:[19,24,38,43,44,48],referenc:43,regardless:[55,66],regener:22,regexp:24,regist:[0,19,24,26,27,33,35,50,55,64,66,68,70],registerschema:26,registersettingsschema:24,registr:0,registri:20,regularli:1,rel:49,relat:[22,61,63],releas:5,reload:0,reload_templ:0,rememb:1,remov:[4,11],render:[11,19,24,45],reorder:1,replac:[1,24,43,46,48,69],repres:12,represent:11,request:[8,11,12,18,20,21,22,23,24,25,26,27,66,68],request_from_arg:8,requir:[0,3,8,12,19,23,24,25,26,27,50],require_logged_in:8,require_method:8,reset:[24,30],reset_fil:24,resetfilesschema:24,respect:45,respons:17,rest:[9,12,18,19,24,42,43,45,46,47],restart:[],restrict:[30,50,53],restructur:[],restructuredtext:[18,19],result:[23,55],retain:30,retriev:[68,69],return_to:[24,26],return_typ:[11,18,24],right:[12,23,24,25,27,30,34,44,46,50,55,61,63,68,69,70],rigid:49,role:[],role_id:27,roll:5,root:[12,20,21],rout:[21,22,23,24,25,26,27],row:[20,45],rst_preview:24,rule:45,run:0,run_change_statu:17,run_timed_task:17,runner:17,salt:12,same:[20,24,26,45,46,48,49,50,55,61,63,70],sampl:42,save:[23,24,27,30,38,52,57,61,69],save_fil:23,scenario:[0,1],schedul:1,schema:[12,15,20],script:11,scss:0,search:[],second:[1,30,70],section:0,section_nam:0,see:[4,5,19,23,30,33,35,42,43,44,50,52,54,55,57,61,63,64,65],seen:26,select:[19,26,27,30,32,34,37,38,40,41,48,50,51,52,54,55,56,57,59,60,61,63,65,69],semi:0,send:[0,20,23,24,26],send_email:20,sender:[0,20],sent:[0,26,66,69,70],separ:[0,11,45,46,50],seri:30,servererror_500:21,set_list:11,setup:0,share:47,shorten:12,should:[0,1,17,20,65],show:[11,20,26,30,35,36,42,43,46,55,61,63,69],shown:[18,30,39,42,43,45,52,54,55,57,59,61,63,66,68,69],sibl:12,side:[30,44,61,63],sign:50,simpl:[45,46],simpli:[34,40,42,43,45,47,61,63],singl:[11,12,17,19,24,30,45],singlevalueexpect:[20,23,24,25,26,27],site:[1,20],size:30,smtp:0,smtp_host:0,softwar:[],some:[19,30],somebodi:45,sometim:[30,50],somewhat:30,sophist:46,sourc:[0,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,45,46,49],sourcecod:[],space:[11,45,46],spam:[66,70],span:[0,19,24,45],specif:[12,19,20,22,23,24,25,26,27,55,65],specifi:[0,1,12,20,24,50,53,65,66,69],sphinx:45,split:[20,45,61,63],spread:49,sql:4,sqla:4,sqlite:3,ssl:0,stabl:45,standard:[0,12],standardis:20,start:[1,5,11,20,26,27,30,45,46,48,70],startup:0,state:[5,19,20,26,30,66],state_machin:19,statement:19,statu:[],step:[0,4,5],still:[17,26],stmt:19,stop:[1,5,11,12,55],stopasgroup:1,storag:0,store:[12,20,26,48],strict:49,structur:[0,4,11],student:[18,55],style:[0,9,14,19],sub:45,subject:20,submit:[24,25,26],subpars:[14,15,17],success:26,successfulli:[5,17],suffix:11,summari:[12,33,52,57,61],supervisorctl:1,support:[0,1,3,4,12,19,20,44,45,47,49,61,63],sure:[4,69],surround:45,syntax:46,system:0,tabl:4,tag:[11,12],take:[4,33],taken:[19,20,35,42,50,54,59,63,65,68,69,70],tar:[3,5],target:[20,24],target_statu:17,target_typ:20,task_id:17,team:19,tele:45,templat:[0,10,11,12,14,24,39,51,60,62],template_for_part:11,template_id:24,term:[42,45,55],test:[0,1,3,4,5,46],text:11,text_formatt:[],than:[1,11,43,45,50],thei:[0,12,20,26,45,50,55,61,63],them:[17,19,30,45,49,52,55,61],theme:[0,14],thi:[0,2,4,5,11,12,17,18,19,20,24,25,26,29,30,31,33,34,35,37,40,41,42,45,48,49,50,51,52,53,54,55,56,57,59,60,61,62,63,65,66,69,70],thing:45,those:[0,26,30,39,50,53,55],though:19,thread:[1,17],three:[5,44,45,52,57,61,64,69],through:[12,30],thu:[26,55],tid:25,timed_task:[],timedelta:[11,12],timedtask:[12,17,25],timestamp:[12,17],timevalid:20,timing_tween_factori:20,titl:[11,12,24,32,33,34,42,43,46,52,54,57,59,61,63],tmp:0,togeth:[11,12,62],token:[12,20,26],tool:45,toolbox:[42,43,44],top:[11,19,30,33,34,36,46,55,68,69,70],transact:0,transform:11,treat:45,tupl:[11,20,24],turn:[11,30],tutor:[53,55,64,69],tutori:[],tween:20,two:[11,32,39,45,46,50,54,59,61,63],txt:14,type:[0,11,12,16,19,20,23,24,25,26,27,32,38,39,42,43,45,46,50,55,61,63],uid:[23,24,26],unauthoris:20,unauthorised_redirect:20,unavail:[53,58,62,64],unblock:55,under:[8,45],underlin:45,understand:49,undon:[30,37,51,56,60,65],unicod:[8,11,12,16,18,20],uniqu:[11,12,17,20],uniqueemailvalid:26,unit:62,unless:45,unsav:30,unsur:42,until:70,updat:0,updatet:25,upgrad:[3,12],upload:[24,39,40,69],upon:26,upper:12,urandom:12,url:[0,11,19,20,21,22,23,24,25,26,27,43,47],usabl:49,usag:19,user:[0,4],user_id:[12,24,27],user_part_progress:12,user_rol:[],userid:26,usernam:[0,4,26],userpartprogress:[12,24],userpartrol:[12,27],users_group:12,users_permiss:12,users_permission_group:12,users_t:19,util:[],valid:[0,8,11,12,20,23,24,25,26,27,68,69,70],validate_kei:0,validation_token:[12,26],valu:[0,11,16,17,19,20,23,24,25,26,27],variabl:[10,26],variant:19,variou:[8,10,20],veri:46,verifi:70,version:[3,5,10,12,20,24],via:[0,1,4,10,12,16,19,26,27,50,53,58,62],video:[],view:[],view_asset:23,view_fil:23,view_part:24,view_part_task:25,virtual:[3,5],virtualenv:1,virtualhost:1,visibl:30,visual:45,wai:[24,45],wait:30,waitress:0,want:[0,19,30,32,38,42,43,45,46,49,50,51,55,56,60,69],webteachingenviron:[3,5],welcom:26,well:1,wendi:19,were:68,what:[12,30,33,42,45,48,52,54,55,57,59,61,62,63],when:[0,3,11,12,24,27,30,39,45,48,50,59,61,63,65,68],whenev:30,where:[1,17,19,26,39,45,55,61,63,68,70],whether:[0,11,12,20,24,26,52,54,62,66],which:[0,1,7,12,19,20,24,30,33,39,41,42,45,46,53,61,63,64,70],white:45,who:[26,50,55,64],wide:45,widest:45,wish:[1,30,31,35,37,40,42,43,45,48,49,50,55,59,63,65,69],within:[0,1,21,45,49,55,66],without:[18,19,40],word:45,work:[0,1,3,30,34,51,55,60,61,63,69],workflow:49,would:[30,45],wrongdomain:26,wsgi:1,wsgiapplic:7,wsgidaemonprocess:1,wsgiprocessgroup:1,wsgiscriptalia:1,wte:[0,4],www:[1,45],xxx:46,xxxxx:47,yet:[4,26],you:[0,1,3,4,5,19,24,26,30,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,68,69,70],your:[4,66,67,68],youtu:47,youtub:[19,47],yyyi:[20,25],zip:[24,30,34,41,48],zipfil:24,zurb:0},titles:["Configuration","Deployment","Administrator Documentation","Installation","Setup","Updating","API Documentation","<code class=\"docutils literal\"><span class=\"pre\">wte</span></code> &#8211; Web Teaching Environment","<code class=\"docutils literal\"><span class=\"pre\">wte.decorators</span></code> &#8211; Decoratorators","<code class=\"docutils literal\"><span class=\"pre\">wte.doc</span></code> &#8211; Docutils Helpers","<code class=\"docutils literal\"><span class=\"pre\">wte.helpers</span></code> &#8211; Helper functionality for views","<code class=\"docutils literal\"><span class=\"pre\">wte.helpers.frontend</span></code> &#8211; Helpers for the frontend display","<code class=\"docutils literal\"><span class=\"pre\">wte.models</span></code> &#8211; Database Models","<code class=\"docutils literal\"><span class=\"pre\">wte.scripts</span></code> &#8211; Administration scripts","<code class=\"docutils literal\"><span class=\"pre\">wte.scripts.configuration</span></code> &#8211; Generate configuration script","<code class=\"docutils literal\"><span class=\"pre\">wte.scripts.database</span></code> &#8211; Database  scripts","<code class=\"docutils literal\"><span class=\"pre\">wte.scripts.main</span></code> &#8211; Administration application","<code class=\"docutils literal\"><span class=\"pre\">wte.scripts.timed_tasks</span></code> &#8211; Script to run timed tasks","<code class=\"docutils literal\"><span class=\"pre\">wte.text_formatter</span></code>","<code class=\"docutils literal\"><span class=\"pre\">wte.text_formatter.docutils_ext</span></code>","<code class=\"docutils literal\"><span class=\"pre\">wte.util</span></code> &#8211; Utility functions","<code class=\"docutils literal\"><span class=\"pre\">wte.views</span></code> &#8211; View handlers","<code class=\"docutils literal\"><span class=\"pre\">wte.views.admin</span></code> &#8211; Admin view handlers","<code class=\"docutils literal\"><span class=\"pre\">wte.views.asset</span></code> &#8211; Assets","<code class=\"docutils literal\"><span class=\"pre\">wte.views.part</span></code> &#8211; Part Backend","<code class=\"docutils literal\"><span class=\"pre\">wte.views.timed_tasks</span></code> &#8211; Timed Tasks Backend","<code class=\"docutils literal\"><span class=\"pre\">wte.views.user</span></code> &#8211; User functionality view handlers","<code class=\"docutils literal\"><span class=\"pre\">wte.views.user_role</span></code> &#8211; Backend for Users in Parts","Web Teaching Environment","User Documentation","HTML Editor Sections","Using Teaching Materials","Module Content","Available Modules","My Modules","Taking a Module","Text Sections","Deleting an Asset","Editing an Asset","Assets","Creating a new Asset","Download Content","Including Assets","Referincing other Modules/Parts/Pages","Editor","Introduction to ReStructured Text","Highlighting Sourcecode","Videos","Importing and Exporting Content","Creating Teaching Materials","Module Access Settings","Delete a Module","Editing a Module","Module","Creating a new Module","User Management","Delete a Page","Editing a Page","Page","Creating a new Page","Delete a Part","Editing a Part","Part","Creating a new Part","Changing the Status","Timed Actions","Forgotten Password","Registration &amp; Login","Logging in","Profile","Registration"],titleterms:{"default":0,"export":48,"function":[10,20,26],"import":48,"new":[30,40,54,59,63,65],access:[3,50],account:69,action:65,add:65,admin:22,administr:[2,13,16],apache2:1,api:6,applic:[0,16],asset:[23,37,38,39,40,42],avail:33,backend:[24,25,27],block:55,chang:[30,55,64,65],configur:[0,4,14],connect:0,content:[32,40,41,42,48],core:3,creat:[40,42,49,54,59,63],criteria:50,databas:[0,3,4,12,15],decor:8,decorator:8,delet:[37,51,56,60,65,69],deploi:1,deploy:1,discard:30,displai:11,doc:9,document:[2,6,29],docutil:9,docutils_ext:19,domain:50,download:[30,41],edit:[38,52,57,61,65,69],editor:[30,40,42,44],environ:[0,7,28],file:30,filter:55,forgotten:66,framework:0,frontend:11,gener:[4,14],handl:0,handler:[21,22,26],helper:[9,10,11],highlight:[45,46],html:30,includ:42,indic:28,initialis:4,instal:3,introduct:45,list:45,log:[0,68],login:67,mail:[0,50],main:16,manag:55,materi:[31,49],mod_wsgi:1,model:12,modul:[32,33,34,35,43,50,51,52,53,54],multipl:50,option:46,other:43,page:[43,56,57,58,59],part:[24,27,43,60,61,62,63],password:[50,66],plain:45,prepar:5,profil:69,pyramid:0,referinc:43,registr:[67,70],remov:55,restart:5,restructur:45,role:55,run:[1,17],script:[13,14,15,16,17],search:[42,43,55],section:[30,36],server:0,session:0,set:[0,50],setup:4,sourcecod:46,sqlalchemi:0,statu:[64,65],string:0,structur:45,supervisord:1,system:3,tab:30,tabl:[28,45],take:35,task:[1,17,25],teach:[0,7,28,31,49],text:[36,45],text_formatt:[18,19],time:[1,17,25,65],timed_task:[17,25],tutori:30,updat:5,user:[26,27,29,55],user_rol:27,util:20,video:47,view:[10,21,22,23,24,25,26,27,30],viewer:30,web:[0,7,28],window:30,workspac:30,wte:[7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],your:69}})