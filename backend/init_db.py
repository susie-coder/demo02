"""
数据库初始化脚本
创建 SQLite 数据库表并插入演示数据

使用方法:
    cd backend
    uv run python init_db.py
"""

import sqlite3
import os
import sys

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lab_homepage.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_tables(conn):
    """创建数据库表"""
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT NOT NULL,
            avatar TEXT DEFAULT '',
            bio TEXT DEFAULT '',
            email TEXT DEFAULT ''
        );

        CREATE TABLE IF NOT EXISTS papers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            authors TEXT NOT NULL,
            journal TEXT DEFAULT '',
            year INTEGER NOT NULL,
            abstract TEXT DEFAULT '',
            doi TEXT DEFAULT ''
        );

        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            date TEXT NOT NULL,
            summary TEXT DEFAULT '',
            content TEXT DEFAULT ''
        );

        CREATE TABLE IF NOT EXISTS research (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT DEFAULT '',
            icon TEXT DEFAULT ''
        );
    """)
    print("[OK] 数据库表创建成功")


def insert_demo_data(conn):
    """插入演示数据"""
    cursor = conn.cursor()

    # 检查是否已有数据
    cursor.execute("SELECT COUNT(*) FROM members")
    if cursor.fetchone()[0] > 0:
        print("数据库已有数据，跳过演示数据插入")
        return

    # 团队成员
    members = [
        ("张明远", "教授 / 实验室主任",
         "https://api.dicebear.com/9.x/initials/svg?seed=张明远&backgroundColor=2563eb&textColor=ffffff",
         "清华大学计算机系教授，博士生导师。主要研究方向为物联网、边缘计算与智能感知。主持国家自然科学基金重点项目、国家重点研发计划等多项课题。",
         "zhangmingyuan@lab.edu.cn"),
        ("李思涵", "副教授",
         "https://api.dicebear.com/9.x/initials/svg?seed=李思涵&backgroundColor=7c3aed&textColor=ffffff",
         "研究方向为无线传感器网络、低功耗物联网通信协议。在 IEEE TMC、ACM SenSys 等顶级期刊和会议上发表论文 40 余篇。",
         "lisihan@lab.edu.cn"),
        ("王浩然", "助理教授",
         "https://api.dicebear.com/9.x/initials/svg?seed=王浩然&backgroundColor=0891b2&textColor=ffffff",
         "研究方向为 AIoT、联邦学习与隐私保护。博士毕业于卡内基梅隆大学，曾获 ACM 最佳博士论文奖。",
         "wanghaoran@lab.edu.cn"),
        ("陈雨桐", "博士研究生",
         "https://api.dicebear.com/9.x/initials/svg?seed=陈雨桐&backgroundColor=059669&textColor=ffffff",
         "研究兴趣包括边缘智能、模型压缩与分布式推理。已在 MobiCom、INFOCOM 等顶会发表论文。",
         "chenyutong@lab.edu.cn"),
        ("赵晓晨", "博士研究生",
         "https://api.dicebear.com/9.x/initials/svg?seed=赵晓晨&backgroundColor=d97706&textColor=ffffff",
         "研究兴趣为智能感知、毫米波通信与室内定位系统。曾获国家奖学金。",
         "zhaoxiaochen@lab.edu.cn"),
        ("刘子涵", "硕士研究生",
         "https://api.dicebear.com/9.x/initials/svg?seed=刘子涵&backgroundColor=db2777&textColor=ffffff",
         "研究嵌入式系统与低功耗物联网设备开发。擅长硬件原型设计与 FPGA 开发。",
         "liuzihan@lab.edu.cn"),
    ]
    cursor.executemany(
        "INSERT INTO members (name, role, avatar, bio, email) VALUES (?, ?, ?, ?, ?)",
        members,
    )

    # 论文成果
    papers = [
        ("EdgeLearner: Communication-Efficient Federated Learning at the Network Edge",
         "Mingyuan Zhang, Sihan Li, Haoran Wang, Yutong Chen",
         "IEEE Transactions on Mobile Computing (TMC)", 2026,
         "本文提出 EdgeLearner 框架，通过自适应模型剪枝和梯度压缩技术，将边缘联邦学习的通信开销降低 67%，同时保持模型精度损失小于 1.2%。实验在真实 IoT 设备集群上验证了该方法的有效性。",
         "10.1109/TMC.2026.0123456"),
        ("mmLoc: Millimeter-Wave Based Indoor Localization with Sub-Centimeter Accuracy",
         "Haoran Wang, Xiaochen Zhao, Mingyuan Zhang",
         "ACM MobiCom 2025", 2025,
         "提出基于毫米波信号的室内定位系统 mmLoc，利用稀疏阵列和压缩感知技术实现亚厘米级定位精度。在复杂室内环境下，平均定位误差仅为 4.2mm。",
         "10.1145/3456789.0123456"),
        ("TinyGuard: Lightweight Anomaly Detection for Resource-Constrained IoT Devices",
         "Sihan Li, Zihan Liu, Mingyuan Zhang",
         "ACM SenSys 2025", 2025,
         "设计了一种适用于资源受限 IoT 设备的轻量级异常检测算法 TinyGuard。该算法仅需 48KB 内存和 12KB 存储空间，在异常检测任务上达到 96.8% 的准确率。",
         "10.1145/3456789.0654321"),
        ("FedPrune: Structured Pruning for Heterogeneous Federated Learning Systems",
         "Yutong Chen, Mingyuan Zhang, Haoran Wang",
         "IEEE INFOCOM 2024", 2024,
         "提出面向异构联邦学习系统的结构化剪枝方法 FedPrune。通过联合优化模型结构和联邦聚合策略，在 Non-IID 数据分布下将模型收敛速度提升 2.3 倍。",
         "10.1109/INFOCOM.2024.0123456"),
        ("A Survey on Edge Intelligence: From Cloud-Edge Collaboration to On-Device Learning",
         "Mingyuan Zhang, Sihan Li, Yutong Chen, Xiaochen Zhao",
         "IEEE Communications Surveys & Tutorials", 2024,
         "综述边缘智能领域的最新进展，涵盖云边协同推理、模型压缩、联邦学习和设备端训练四大技术路线，并展望了边缘大模型部署的未来方向。",
         "10.1109/COMST.2024.0123456"),
        ("LoRaSense: Long-Range Environmental Monitoring with LoRa Backscatter",
         "Zihan Liu, Sihan Li, Xiaochen Zhao",
         "ACM/IEEE IPSN 2024", 2024,
         "利用 LoRa 反向散射技术实现低功耗远距离环境监测。设计无源感知标签可在 500m 范围内以 0.1μW 功耗回传传感数据，电池寿命超过 5 年。",
         "10.1145/3456789.0789012"),
    ]
    cursor.executemany(
        "INSERT INTO papers (title, authors, journal, year, abstract, doi) VALUES (?, ?, ?, ?, ?, ?)",
        papers,
    )

    # 新闻动态
    news_items = [
        ("实验室论文 EdgeLearner 被 IEEE TMC 接收",
         "2026-05-20",
         "张明远教授团队的联邦学习研究取得重要突破，论文被移动计算领域顶级期刊接收。该工作显著降低了边缘联邦学习的通信开销。",
         "经过两年的研究与实验，张明远教授团队提出的 EdgeLearner 框架正式被 IEEE Transactions on Mobile Computing (TMC) 接收。该框架通过自适应模型剪枝和梯度压缩技术，在保证模型精度的前提下将通信开销降低 67%，为边缘智能的实际部署提供了高效的解决方案。论文第一作者为张明远教授，合作者包括李思涵副教授、王浩然助理教授和陈雨桐博士。"),
        ("王浩然助理教授获 ACM 杰出青年科学家奖",
         "2026-04-15",
         "实验室王浩然助理教授因其在毫米波感知与定位领域的突出贡献，荣获 ACM 杰出青年科学家奖。",
         "ACM（国际计算机学会）宣布王浩然助理教授获得 2025 年度 ACM 杰出青年科学家奖，以表彰他在毫米波感知与室内定位领域的开创性工作。王浩然助理教授在 mmLoc 系统中实现了亚厘米级室内定位精度，该成果已在智能工厂和智慧医疗场景中得到初步应用。"),
        ("实验室承办 IEEE SECON 2026 国际会议",
         "2026-03-01",
         "经 IEEE 通信学会批准，智能物联网实验室将承办 IEEE SECON 2026 国际会议，张明远教授担任大会主席。",
         "IEEE 通信学会正式批准由本实验室承办 IEEE International Conference on Sensing, Communication, and Networking (SECON) 2026。会议将于 2026 年 9 月在北京举行，张明远教授担任大会主席，李思涵副教授担任程序委员会主席。这是该会议首次在中国大陆举办，体现了国际学术界对本实验室研究水平的高度认可。"),
        ("实验室在 ISCA 2025 获得最佳演示奖",
         "2025-12-10",
         "陈雨桐博士和赵晓晨博士在 ISCA 2025 会议现场演示联邦学习边缘推理系统，获得最佳演示奖。",
         "在 ACM/IEEE International Symposium on Computer Architecture (ISCA) 2025 会议上，陈雨桐博士和赵晓晨博士联合演示了「面向异构边缘设备的联邦推理加速系统」，凭借出色的现场表现和技术创新性，荣获大会最佳演示奖（Best Demo Award）。评审委员会称赞该系统「在真实边缘设备上展示了令人印象深刻的性能」。"),
        ("实验室获国家自然科学基金重点项目资助",
         "2025-09-01",
         "张明远教授主持申报的「面向工业物联网的边缘智能理论与关键技术」获批国家自然科学基金重点项目，总经费 300 万元。",
         "国家自然科学基金委员会公布了 2025 年度重点项目评审结果，张明远教授主持申报的「面向工业物联网的边缘智能理论与关键技术」成功获批，项目总经费 300 万元，执行期 2026 年 1 月至 2029 年 12 月。该项目将系统研究边缘智能在工业场景中的模型压缩、分布式推理和资源调度等关键问题。"),
    ]
    cursor.executemany(
        "INSERT INTO news (title, date, summary, content) VALUES (?, ?, ?, ?)",
        news_items,
    )

    # 研究方向
    research_areas = [
        ("边缘计算与边缘智能", "研究边缘设备上的智能计算范式，包括模型压缩、分布式推理和边缘-云端协同。探索在计算、存储、能耗受限的边缘设备上部署 AI 模型的理论与方法。", "🧠"),
        ("物联网通信协议", "设计面向低功耗、远距离、高可靠场景的新型 IoT 通信协议。涵盖 LoRa 反向散射、毫米波通信、超宽带定位等前沿技术。", "📡"),
        ("联邦学习与隐私计算", "研究分布式数据场景下的隐私保护机器学习方法。包括联邦优化算法、差分隐私保护、安全多方计算及其在 IoT 场景的应用。", "🔒"),
        ("智能感知与定位", "利用无线信号（WiFi、毫米波、超声波）实现高精度环境感知与目标定位。应用于智能家居、工业检测和医疗健康等领域。", "📍"),
        ("低功耗嵌入式系统", "设计亚毫瓦级功耗的嵌入式 AI 硬件平台，包括专用加速器设计、能量采集技术和实时操作系统优化。", "⚡"),
        ("AIoT 应用与系统", "将 AI + IoT 技术落地于智慧工厂、智慧城市和智慧医疗等场景。构建端到端原型系统，验证技术在真实环境中的性能与可靠性。", "🏭"),
    ]
    cursor.executemany(
        "INSERT INTO research (name, description, icon) VALUES (?, ?, ?)",
        research_areas,
    )

    conn.commit()
    print(f"[OK] 演示数据插入成功（{len(members)} 名成员、{len(papers)} 篇论文、{len(news_items)} 条新闻、{len(research_areas)} 个研究方向）")


def main():
    conn = get_connection()
    try:
        create_tables(conn)
        insert_demo_data(conn)
        print(f"\n数据库文件: {DB_PATH}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
