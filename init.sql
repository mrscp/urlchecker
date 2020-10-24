SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `urlcheckhistory`
-- ----------------------------
DROP TABLE IF EXISTS `urlcheckhistory`;
CREATE TABLE `urlcheckhistory` (
  `recid` int(11) NOT NULL AUTO_INCREMENT,
  `urlid` int(11) NOT NULL,
  `CheckTime` datetime NOT NULL,
  `CheckResult` bit(1) NOT NULL,
  PRIMARY KEY (`recid`),
  KEY `urlid` (`urlid`),
  CONSTRAINT `urlcheckhistory_ibfk_1` FOREIGN KEY (`urlid`) REFERENCES `urls` (`urlid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of urlcheckhistory
-- ----------------------------
INSERT INTO `urlcheckhistory` VALUES ('1', '1', '2020-10-22 00:05:00', '');
INSERT INTO `urlcheckhistory` VALUES ('2', '2', '2020-10-22 00:05:00', '');
INSERT INTO `urlcheckhistory` VALUES ('3', '1', '2020-10-22 00:10:00', '');
INSERT INTO `urlcheckhistory` VALUES ('4', '2', '2020-10-22 00:10:00', '');

-- ----------------------------
-- Table structure for `urls`
-- ----------------------------
DROP TABLE IF EXISTS `urls`;
CREATE TABLE `urls` (
  `urlid` int(11) NOT NULL AUTO_INCREMENT,
  `urladdress` varchar(255) NOT NULL,
  `IntervalMinutes` int(11) NOT NULL DEFAULT '0',
  `UseKeywords` bit(1) NOT NULL,
  `Keywords` varchar(255) DEFAULT NULL,
  `LastCheckTime` datetime DEFAULT NULL,
  `IsActive` bit(1) NOT NULL,
  PRIMARY KEY (`urlid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of urls
-- ----------------------------
INSERT INTO `urls` VALUES ('1', 'https://google.com', '5', '', null, null, '');
INSERT INTO `urls` VALUES ('2', 'https://yahoo.com', '10', '', 'google,welcome,hello', null, '');
