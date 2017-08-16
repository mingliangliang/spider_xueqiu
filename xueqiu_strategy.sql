DROP TABLE IF EXISTS xueqiu_strategy;
CREATE TABLE xueqiu_strategy (
  f_id int(11) NOT NULL AUTO_INCREMENT,
  f_title varchar(64) NOT NULL COMMENT '策略名称',
  f_sign varchar(64) DEFAULT NULL COMMENT '策略标签',
  f_slogan varchar(128) DEFAULT NULL COMMENT '策略标语',
  f_detail varchar(512) DEFAULT NULL COMMENT '策略说明',
  f_updatetime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '插入时间戳',
  UNIQUE KEY (f_title),
  KEY f_id (f_id)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;