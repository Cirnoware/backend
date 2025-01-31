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

 Date: 31/01/2025 15:40:10
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
INSERT INTO `home` VALUES (1, 'data1145', 'this is data 2', '2025-01-27 22:57:30');
INSERT INTO `home` VALUES (3, '1122', 'this is data 3', '2025-01-28 22:57:43');
INSERT INTO `home` VALUES (20250131005955, 'data5', 'this is data5', '2025-01-31 00:59:55');
INSERT INTO `home` VALUES (20250131152045, '114', 'this is 20250131152045', '2025-01-31 15:20:45');
INSERT INTO `home` VALUES (20250131153721, '514', 'this is 20250131153721', '2025-01-31 15:37:21');

SET FOREIGN_KEY_CHECKS = 1;
