/*
 Navicat Premium Data Transfer

 Source Server         : local
 Source Server Type    : MySQL
 Source Server Version : 80300 (8.3.0)
 Source Host           : localhost:3306
 Source Schema         : eeeic

 Target Server Type    : MySQL
 Target Server Version : 80300 (8.3.0)
 File Encoding         : 65001

 Date: 31/01/2025 14:02:42
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for home
-- ----------------------------
DROP TABLE IF EXISTS `home`;
CREATE TABLE `home`  (
  `id` bigint NULL DEFAULT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `data` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `create_time` datetime NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of home
-- ----------------------------
INSERT INTO `home` VALUES (2, 'data2', 'this is data 2', '2025-01-27 22:57:30');
INSERT INTO `home` VALUES (3, 'data3', 'this is data 3', '2025-01-28 22:57:43');
INSERT INTO `home` VALUES (1, 'data114', 'this is data 1', '2025-01-26 23:50:16');
INSERT INTO `home` VALUES (4, 'data4', 'this is data 4', '2025-01-31 00:22:35');
INSERT INTO `home` VALUES (20250131005955, 'data5', 'this is data5', '2025-01-31 00:59:55');

SET FOREIGN_KEY_CHECKS = 1;
