# import pandas as pd
import os
import sys

os.chdir('/opt/tiger/toutiao/log/run/')
file_list = os.listdir('.')
PSM_name = ''
file_name = ''
for f in file_list:
    if 'run.log' in f:
        PSM_name = f.split('.run')[0]
        file_name = f
if PSM_name == '':
    sys.exit()
psm_map = {
    "live.room.goroom": "live/room",
    "live.screenshot_streaming_review.callback": "live/review_streaming_callback",
    "live.room.live_record": "live/liverecord",
    "live.review_goscript.review_task_from_nsq": "live/screenshot_streaming_review",
    "aweme.api.golive": "aweme/golive_api",
    "live.review_goservice.tcs_callback": "live/review_tcs_callback",
    "live.audio_review.enqueue_task": "live/audio_enqueue_task",
    "live.review_goscript.review_task": "live/screenshot_streaming_review",
    "live.wallet.gowallet": "live/wallet",
    "webcast.room.manager": "webcast/room_manager",
    "webcast.anchor.core": "webcast/anchor_core",
    "webcast.feed.api": "webcast/feed_api",
    "webcast.user.base": "webcast/user",
    "webcast.user.relation": "webcast/user_relation",
    "webcast.user.pack": "webcast/user_pack",
    "webcast.room.api": "webcast/room_api",
    "webcast.setting.api": "webcast/setting_api",
    "webcast.user.api": "webcast/user_api",
    "webcast.profit.api": "webcast/profit_api",
    "webcast.ranklist.base": "webcast/ranklist",
    "webcast.ranklist.update": "webcast/ranklist_update",
    "webcast.ranklist.api": "webcast/ranklist_api",
    "webcast.review.review": "webcast/review",
    "webcast.room.pack": "webcast/room_pack",
    "webcast.room.delegate": "webcast/room_delegate",
    "webcast.wallet.api": "webcast/wallet_api",
    "live.room.config": "live/config",
    "ies.order.channel": "ies/order_channel",
    "webcast.union.union": "webcast/union",
    "webcast.battle.update": "webcast/battle_update",
    "webcast.platform.sign": "webcast/sign",
    "webcast.goods.base": "webcast/goods_base",
    "live.sdim.msgserver": "live/sdim_msgserver",
    "live.sdim.metaserver": "live/sdim_metaserver",
    "webcast.battle.record": "webcast/battle_record",
    "live.review.review_pipline_service": "live/review_pipline_service",
    "webcast.battle.core": "webcast/battle_core",
    "webcast.order.core": "webcast/order",
    "webcast.linkmic_audience.api": "webcast/linkmic_audience_api",
    "webcast.feedback.base": "webcast/feedback",
    "webcast.linkmic.core": "webcast/linkmic_core",
    "webcast.data.api": "webcast/data_api",
    "webcast.diamond.api": "webcast/diamond_api",
    "webcast.luckymoney.luckymoney": "webcast/luckymoney_service",
    "live.review.reexam_service": "live/reexam_service",
    "webcast.grade.scripts": "webcast/grade_scripts",
    "webcast.grade.worker": "webcast/grade_worker",
    "webcast.battle.check_user_alive": "webcast/battle_workers",
    "webcast.stats.stats": "webcast/stats_stats",
    "webcast.platform.union_invite": "webcast/union_invite",
    "webcast.room.pack_backup": "webcast/room_pack_backup",
    "live.review.playerkilling": "live/review_playerkilling",
    "live.review.reexam_general_callback": "live/reexam_callback",
    "webcast.data.object": "webcast/data_object",
    "webcast.script.portal": "webcast/profit_script_portal",
    "webcast.lottery.core": "webcast/lottery_core",
    "webcast.lottery.consumer": "webcast/lottery_workers",
    "ies.dm.task_store": "ies/task_store",
    "ies.dm.task_meta": "ies/dm_task_meta",
    "webcast.data.hikari": "webcast/data_hikari",
    "webcast.data.src_anchor_fan_ticket": "webcast/data_src_anchor_fan_ticket",
    "webcast.sort.core": "webcast/sort_core",
    "webcast.diamond.filter": "webcast/diamond_filter",
    "webcast.review.ban": "webcast/review_ban",
    "webcast.platform.union_anchor_base": "webcast/union_anchor_base",
    "webcast.linkmic_audience.base": "webcast/linkmic_audience",
    "webcast.platform.union_task": "webcast/union_task",
    "webcast.room.online_room": "webcast/online_room",
    "webcast.union.reward_grant": "webcast/union_reward_grant",
    "webcast.room.permission": "webcast/room_permission",
    "webcast.data.kushim": "webcast/data_kushim",

    "webcast.room.interaction": "webcast/room_interaction",
    "live.review.content_tag": "live/review_content_tag",
    "webcast.profit.core": "webcast/profit_core",
    "webcast.platform.account": "webcast/account",
    "ma.open.payment_order_api": "developer/ma_payment_order_api",
    "webcast.review.api": "webcast/review_api",
    "webcast.room.filter": "webcast/room_filter",
    "ies.dm.usergroup": "ies/dm_usergroup",
    "webcast.room_filter.script": "webcast/room_filter_script",
    "webcast.pack.scene": "webcast/pack_scene",
    "webcast.social.music": "webcast/social_music",
    "live.review.cache": "live/review_cache",
    "wallet.merchant.core": "webcast/wallet_merchant_core",
    "webcast.room_script.room_user_front": "webcast/room_user",
    "wallet.pay.core": "webcast/wallet_pay_core",
    "webcast.linkmic.biz": "webcast/linkmic_biz",
    "wallet.account.mapping": "webcast/wallet_account_mapping",
    "ma.open.match_make": "developer/ma_match_make",
    "webcast.review.config": "webcast/review_config",
    "webcast.review.pack": "webcast/review_pack",
    "webcast.dlottery.api": "webcast/dlottery_api",
    "webcast.dlottery.consumer": "webcast/dlottery_consumer",
    "webcast.front.config": "webcast/front_config",
    "webcast.growth.core": "webcast/growth_core",
    "webcast.battle.match": "webcast/battle_match",
    "webcast.review.punish": "webcast/review_punish",
    "webcast.game.feed": "webcast/game_feed",
    "webcast.growth.worker": "webcast/growth_worker",
    "webcast.data.hsap": "webcast/data_hsap",
    "webcast.faction.core": "webcast/faction_core",
    "live.review.rule": "live/review_rule",
    "webcast.data.hsap_task_manager": "webcast/data_hsap_task_manager",
    "webcast.data.hsap_task_runner": "webcast/data_hsap_task_runner",
    "webcast.anchor.permission": "webcast/anchor_permission",
    "webcast.room.api_open": "webcast/room_api_open",
    "webcast.feed.api_open": "webcast/feed_api_open",
    "webcast.xactivity.task_event_consumer": "webcast/xactivity_task_event_consumer",
    "webcast.creator.api": "webcast/creator_api",
    "webcast.user.api_open": "webcast/user_api_open",
    "webcast.hproject.control_center": "webcast/hproject_control_center",
    "webcast.hproject.hloop": "webcast/hproject_hloop",
    "webcast.gamelive.api": "webcast/gamelive_api",
    "webcast.room_script.room_user_front_pb": "webcast/room_user",
    "webcast.review.sensitive": "webcast/review_sensitive",
    "webcast.review.feature": "webcast/review_feature",
    "webcast.interaction.api": "webcast/interaction_api",
    "webcast.data.hsap_data_center": "webcast/data_hsap_data_center",
    "webcast.show.api": "webcast/show_api",
    "webcast.show.core": "webcast/show_core",
    "webcast.show.pack": "webcast/show_pack",
    "webcast.show.show": "webcast/show",
    "webcast.platform.authenticate": "webcast/authenticate",
    "webcast.show.data": "webcast/show_data",
    "webcast.growth.task": "webcast/growth_task",
    "webcast.growth.task_event": "webcast/growth_task_event",
    "webcast.data.sofa_pv_mock_service": "webcast/data_sofa_pv_mock_service",
    "webcast.growth.dress": "webcast/growth_dress",
    "webcast.linkmic.online_linkmic": "webcast/online_linkmic",
    "ark.basic.api": "webcast/ark_basic_api",
    "webcast.platform.schema": "webcast/schema",
    "webcast.linkmic.online_linkmic_all": "webcast/online_linkmic_all",
    "webcast.data.retrieve": "webcast/data_retrieve",
    "webcast.union.data": "webcast/union_data",
    "ark.data.api": "webcast/ark_data_api",
    "ark.account.api": "webcast/ark_account_api",
    "webcast.platform_account.bind": "webcast/platform_account_bind",
    "webcast.open.appinfo": "webcast/open_appinfo",
    "ark.growth.api": "webcast/ark_growth_api",
    "webcast.show.filter": "webcast/show_filter",
    "ark.data_ext.api": "webcast/ark_data_ext_api",
    "webcast.preorder.core": "webcast/preorder",
    "webcast.ktv.api": "webcast/ktv_api",
    "webcast.platform.union_decision": "webcast/union_decision",
    "webcast.review.punish_proxy": "webcast/review_punish_proxy",
    "webcast.consume.core": "webcast/consume_core",
    "webcast.ark_opr.team": "webcast/ark_opr_team",
    "webcast.platform.oa_approve": "webcast/oa_approve",
    "webcast.privilege.core": "webcast/privilege_core",
    "webcast.privilege.api": "webcast/privilege_api",
    "webcast.user.relation_script": "webcast/user_relation_script",
    "wallet.content_trade.order_core": "webcast/wallet_content_trade_order",
    "wallet.content_trade.relation_core": "webcast/wallet_content_trade_relation",
    "webcast.activity.leucothea": "webcast/activity_leucothea",
    "webcast.clear.split_ratio": "webcast/clear_split_ratio",
    "webcast.fulfillment.business": "webcast/fulfillment_business",
    "live.sdim.proxy": "live/sdim_proxy",
    "webcast.feed.base": "webcast/feed_base",
    "webcast.evaluation.base": "webcast/evaluation_base",
    "wallet.diamond.api": "webcast/wallet-diamond-api",
    "webcast.platform.union_workflow": "webcast/union_workflow",
    "webcast.data.resource_manager": "webcast/data_resource_manager",
    "webcast.room.creator_api": "webcast/room_creator_api",
    "webcast.room.creator": "webcast/room_creator",
    "webcast.review.feature_manager": "webcast/review_feature_manager",
    "webcast.review.function_manage": "webcast/review_function_manage",
    "wallet.account.control": "webcast/wallet-account-control",
    "webcast.ploy.res_limit": "webcast/resource_control",
    "webcast.room.extra_incr_fix_double_set": "live/live_record",
    "webcast.linkmic.controller": "webcast/linkmic_controller",
    "wallet.trade_coin.payment": "webcast/wallet_trade_coin_payment",
    "webcast.platform.approval_flow": "webcast/approval_flow",
    "webcast.linkmic_friend.consumer": "webcast/linkmic_friend_consume",
    "webcast.room.enter_api": "webcast/enter_api",
    "webcast.interaction.chat_api": "webcast/interaction_chat_api",
    "webcast.disposal.flow_control": "webcast/disposal_flow_control",
    "webcast.lottery.draw": "webcast/lottery_draw",
    "webcast.platform.batch_schedule": "webcast/batch_schedule",
    "webcast.platform.batch_schedule_consumer": "webcast/batch_schedule_consumer",
    "webcast.linkmic_profit.api": "webcast/linkmic_profit_api",
    "webcast.linkmic_profit.core": "webcast/linkmic_profit_core",
    "ma.open.payment_withdraw": "developer/ma_payment_withdraw",
    "webcast.gamecp.attribute": "webcast/gamecp_attribute",
    "webcast.review.hawk_rule": "webcast/review_hawk_rule",
    "webcast.gamecp.open_platform": "webcast/gamecp_open_platform",
    "webcast.platform.contract": "webcast/platform_contract",
    "webcast.gamecp_activity.api": "webcast/gamecp_activity_api",
    "wallet.clear.order_recver": "webcast/wallet_clear_order_recver",
    "wallet.promotion.core": "webcast/wallet_promotion_core",
    "wallet.open.merchant_order": "webcast/wallet_open_merchant_order",
    "wallet.open.sakura": "webcast/wallet_open_sakura",
    "webcast.review.action_audit": "webcast/action_audit",
    "wallet.settle.trigger": "webcast/wallet_settle_trigger",
    "webcast.gameplay.admin": "webcast/gameplay_admin",
    "wallet.settle.order_center": "webcast/wallet_settle_order_center",
    "wallet.clear.charge_core": "webcast/wallet_clear_charge_core",
    "wallet.clear.bill_core": "webcast/wallet_clear_bill_core",
    "wallet.open.merchant_conf": "webcast/wallet_open_merchant_conf",
    "webcast.growth.center": "webcast/growth_center",
    "webcast.review.queue_process": "webcast/review_queue_process",
    "webcast.consume.api": "webcast/consume_api",
    "webcast.room.extra_admin": "webcast/extra_admin",
    "webcast.platform.resource_distribution": "webcast/resource_distribution",
    "webcast.gamecp.pad": "webcast/gamecp_pad",
    "webcast.platform.resource_distribution_consumer": "webcast/resource_distribution_consumer",
    "webcast.growth.user_platform": "webcast/growth_user_platform",
    "webcast.gamecp.contract": "webcast/gamecp_contract",
    "webcast.gamecp.task": "webcast/gamecp_task",
    "wallet.tax.core": "webcast/wallet-tax-core",
    "webcast.gameorg.platform": "webcast/gameorg_platform",
    "webcast.anchor.category": "webcast/anchor_category",
    "webcast.boe.platform": "webcast/boe_platform",
    "webcast.data.bifrost": "webcast/data_bifrost",
    "webcast.show.sort": "webcast/show_sort",
    "webcast.growth.touch": "webcast/growth_touch",
    "wallet.tax.core_task": "webcast/wallet_tax_core_task",
    "webcast.review.frodo_action": "webcast/review_frodo_action",
    "ark.base.corporation": "webcast/ark_base_corporation",
    "live.room.liverecord": "live/live_record",
    "wallet.open.settle": "webcast/wallet_open_settle",
    "wallet.open.fee": "webcast/wallet_open_fee",
    "webcast.open.recommend_proxy": "webcast/open_recommend_proxy",
    "webcast.ranklist.core": "webcast/ranklist_core",
    "wallet.open.channel": "webcast/wallet_open_channel",
    "webcast.capital.core": "webcast/capital_core",
    "webcast.capital.base": "webcast/capital_base",
    "wallet.open.channel_api": "webcast/wallet_open_channel_api",
    "webcast.open.xigua_live": "webcast/open_xigua_live",
    "webcast.game_station.anchor": "webcast/game_station_anchor",
    "webcast.growth.biz": "webcast/growth_biz",
    "webcast.op_strategy.reward": "webcast/op_strategy_reward",
    "webcast.op_strategy.processor": "webcast/op_strategy_processor",
    "webcast.op_strategy.event": "webcast/op_strategy_event",
    "webcast.op_strategy.feature": "webcast/op_strategy_feature",
    "webcast.op_strategy.configured": "webcast/op_strategy_configured",
    "webcast.common.meta_data": "webcast/meta_data",
    "webcast.review.punish_gateway": "webcast/review_punish_gateway",
    "webcast.room_filter.online_room_sync": "webcast/room_filter_online_room_sync",
    "webcast.room_channel.manager": "webcast/room_channel_manager",
    "webcast.room.data_sdk_refresher": "webcast/data_sdk_refresher",
    "webcast.room.data_sdk_refresher_consumer": "webcast/data_sdk_refresher_consumer",
    "ma.open.event_tracking": "open/ma_open_event_tracking",
    "webcast.user.connection": "webcast/user_connection",
    "douyin_cloud.gateway.ingress": "douyincloud/gateway_ingress",
    "douyincloud.arch.logs_consumer": "douyincloud/logs_consumer",
    "douyincloud.arch.metrics_consumer": "douyincloud/metrics_consumer",
    "wallet.open.refund": "webcast/wallet_open_refund",
    "webcast.profit.event_proxy": "webcast/profit_event_proxy",
    "webcast.review.monitor": "webcast/review_monitor",
    "douyin_cloud.deploy.core": "douyincloud/deploy",
    "webcast.douyincloud.auth_service_logs_consumer": "douyincloud/logs_consumer",
    "webcast.act.trigger": "webcast/act_trigger",
    "webcast.room_script.room_user_relation": "webcast/room_user_relation",
    "douyin_cloud.gateway.config": "douyincloud/cloud_config_service_tce",
    "webcast.game.evaluation": "webcast/game_evaluation",
    "webcast.common.cache_manager": "webcast/meta_cache_manager",
    "wallet.open.match_make": "webcast/wallet_open_match_make",
    "webcast.sports.api": "webcast/sports_api",
    "webcast.sports.venue_api": "webcast/venue_api",
    "douyin_cloud.alarm.base": "douyincloud/alarm_base",
    "webcast.linkmic.ecology": "webcast/linkmic_ecology",
    "webcast.game.creator": "webcast/game_creator",
    "webcast.review.task_pool": "webcast/review_task_pool",
    "webcast.sports.venue_push": "webcast/venue_push",
    "webcast.linkmic.kernel": "webcast/linkmic_kernel",
    "webcast.sports.quiz_api": "webcast/sports_quiz_api",
    "webcast.sports.host_team": "webcast/sports_host_team",
    "webcast.sports.quiz_core": "webcast/sports_quiz_core",
    "webcast.sports.activity_api": "webcast/sports_activity_api",
    "webcast.sports.activity_base": "webcast/sports_activity_base",
    "webcast.game.detail": "webcast/game_detail",
    "webcast.sports.redpacket_core": "webcast/sports_redpacket_core",
    "webcast.sports.redpacket_api": "webcast/sports_redpacket_api",
    "wallet.open.guarantee_pay": "webcast/wallet_open_guarantee_pay",
    "webcast.sports.wallet_base": "webcast/sports_wallet_base",
    "webcast.sports.wallet_api": "webcast/sports_wallet_api",
    "webcast.sports.tour_review": "webcast/sports_tour_review",
    "webcast.sports.quiz_card": "webcast/sports_quiz_card",
    "webcast.sports.quiz_consume": "webcast/sports_quiz_consume",
    "douyin_cloud.deploy.process": "douyincloud/deploy_process",
    "webcast.platform.wccvolc": "webcast/wcc",
    "webcast.gameark.base": "webcast/gameark_base",
    "webcast.sports.quiz_settle": "webcast/sports_quiz_settle",
    "webcast.sports.redpacket_consumer": "webcast/sports_redpacket_consumer",
    "webcast.sports.watch_live_achievement": "webcast/watch_live_achievement",
    "webcast.game.creator_ops": "webcast/game_creator_ops",
    "webcast.ugc_config.manager": "webcast/ugc_config_manager",
    "webcast.op_strategy.adapter": "webcast/op_strategy_adapter",
    "webcast.op_strategy.task_api": "webcast/op_strategy_task_api",
    "webcast.hotkey.broker": "webcast/hotkey_broker",
    "webcast.scheduler.delay": "webcast/scheduler_delay",
    "webcast.wds.metaserver": "webcast/wds_metaserver",
    "webcast.wds.dataserver": "webcast/wds_dataserver",
    "webcast.wds.informer": "webcast/wds_informer"}
git = psm_map[PSM_name]
consider_list = [git]

file = open(file_name, encoding='unicode_escape')

find_race_begin = False
race_list = []

for line in file.readlines():
    if '==================' in line and not find_race_begin:  # data race
        find_race_begin = True
        race_buffer = []
        continue
    elif '==================' in line and find_race_begin:  # data race
        find_race_begin = False
        race_list.append(race_buffer)
        continue
    elif find_race_begin:
        race_buffer.append(line)

webcast_race = {}  # key:error position, value:race count
race_set = set()
for race in race_list:
    step_deep = 0
    is_webcast_race = False
    for i in range(len(race)):
        if 'coverage' in race[i]:
            continue
        if 'Goroutine' in race[i] or 'goroutine' in race[i]:
            step_deep = 0
        step_deep += 1
        source_code = race[i]
        if ('code.byted.org/' + git) in source_code and ":" in source_code and step_deep < 4:
            pos = source_code.split('code.byted.org/')[-1].split(' ')[0]
            # webcast_race[pos] = race
            if pos in webcast_race.keys():
                webcast_race[pos] += 1
            else:
                webcast_race[pos] = 1
                race_set.add(''.join(race))

consider_dic = {}
for k, v in webcast_race.items():
    for psm in consider_list:
        if psm in k:
            consider_dic[k] = v

# df = pd.DataFrame([consider_dic])
# df = df.T
# df.to_csv(file_name.split('.run.log.')[0] + '.csv')
# print(df)
print(len(race_set))
print("=========")
for e in race_set:
    print(e)
    print("=========")

