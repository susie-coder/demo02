"""
智能物联网实验室官网 - Flask 后端
提供 RESTful API，从 SQLite 数据库查询数据
"""

import os
import sqlite3
from flask import Flask, g, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lab_homepage.db")


def get_db():
    """获取数据库连接（请求级别缓存）"""
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


@app.teardown_appcontext
def close_db(exception):
    """请求结束后关闭数据库连接"""
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db_if_needed():
    """如果数据库文件不存在，自动运行初始化脚本"""
    if not os.path.exists(DB_PATH):
        print(f"[INFO] 数据库文件 {DB_PATH} 不存在，正在自动初始化...")
        try:
            import init_db
            init_db.main()
            print("[INFO] 数据库初始化完成")
        except Exception as e:
            print(f"[ERROR] 数据库初始化失败: {e}")


# ─── API 接口 ───────────────────────────────────────────────

@app.route("/api/members", methods=["GET"])
def get_members():
    """获取团队成员列表"""
    db = get_db()
    rows = db.execute(
        "SELECT id, name, role, avatar, bio, email FROM members ORDER BY id"
    ).fetchall()
    return jsonify([dict(row) for row in rows])


@app.route("/api/members", methods=["POST"])
def add_member():
    """新增团队成员"""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "请求体不能为空"}), 400

    required = ["name", "role"]
    for field in required:
        if field not in data or not data[field]:
            return jsonify({"error": f"缺少必填字段: {field}"}), 400

    db = get_db()
    cursor = db.execute(
        "INSERT INTO members (name, role, avatar, bio, email) VALUES (?, ?, ?, ?, ?)",
        (
            data["name"],
            data["role"],
            data.get("avatar", ""),
            data.get("bio", ""),
            data.get("email", ""),
        ),
    )
    db.commit()
    new_id = cursor.lastrowid
    row = db.execute("SELECT id, name, role, avatar, bio, email FROM members WHERE id = ?", (new_id,)).fetchone()
    return jsonify(dict(row)), 201


@app.route("/api/papers", methods=["GET"])
def get_papers():
    """获取论文列表"""
    db = get_db()
    rows = db.execute(
        "SELECT id, title, authors, journal, year, abstract, doi FROM papers ORDER BY year DESC, id DESC"
    ).fetchall()
    return jsonify([dict(row) for row in rows])


@app.route("/api/news", methods=["GET"])
def get_news():
    """获取新闻动态列表"""
    db = get_db()
    rows = db.execute(
        "SELECT id, title, date, summary, content FROM news ORDER BY date DESC, id DESC"
    ).fetchall()
    return jsonify([dict(row) for row in rows])


@app.route("/api/news", methods=["POST"])
def add_news():
    """新增新闻动态"""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "请求体不能为空"}), 400

    required = ["title", "date"]
    for field in required:
        if field not in data or not data[field]:
            return jsonify({"error": f"缺少必填字段: {field}"}), 400

    db = get_db()
    cursor = db.execute(
        "INSERT INTO news (title, date, summary, content) VALUES (?, ?, ?, ?)",
        (
            data["title"],
            data["date"],
            data.get("summary", ""),
            data.get("content", ""),
        ),
    )
    db.commit()
    new_id = cursor.lastrowid
    row = db.execute("SELECT id, title, date, summary, content FROM news WHERE id = ?", (new_id,)).fetchone()
    return jsonify(dict(row)), 201


@app.route("/api/research", methods=["GET"])
def get_research():
    """获取研究方向列表"""
    db = get_db()
    rows = db.execute(
        "SELECT id, name, description, icon FROM research ORDER BY id"
    ).fetchall()
    return jsonify([dict(row) for row in rows])


# ─── 启动 ───────────────────────────────────────────────────

if __name__ == "__main__":
    init_db_if_needed()
    print("[INFO] 后端服务启动于 http://localhost:3001")
    app.run(host="127.0.0.1", port=3001, debug=True)
