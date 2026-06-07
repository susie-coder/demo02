import styles from './Footer.module.css';

export default function Footer() {
  return (
    <footer className={styles.footer}>
      <div className={styles.inner}>
        <div className={styles.brand}>
          <span className={styles.logo}>IIoT Lab</span>
          <p className={styles.brandDesc}>
            智能物联网实验室，成立于 2018 年，致力于边缘计算、物联网通信与 AIoT 系统的前沿研究。
          </p>
        </div>

        <div className={styles.cols}>
          <div className={styles.col}>
            <h4 className={styles.colTitle}>联系方式</h4>
            <p>北京市海淀区清华大学<br />信息技术大楼 501 室</p>
            <p>lab@iiot.edu.cn</p>
            <p>+86 10 6278-XXXX</p>
          </div>
          <div className={styles.col}>
            <h4 className={styles.colTitle}>快速导航</h4>
            <ul className={styles.linkList}>
              <li><a href="#research">研究方向</a></li>
              <li><a href="#members">团队成员</a></li>
              <li><a href="#papers">论文成果</a></li>
              <li><a href="#news">新闻动态</a></li>
            </ul>
          </div>
          <div className={styles.col}>
            <h4 className={styles.colTitle}>合作单位</h4>
            <ul className={styles.linkList}>
              <li>清华大学计算机系</li>
              <li>国家自然科学基金委</li>
              <li>IEEE / ACM</li>
            </ul>
          </div>
        </div>
      </div>

      <div className={styles.bottom}>
        <p>&copy; {new Date().getFullYear()} 智能物联网实验室. All rights reserved.</p>
      </div>
    </footer>
  );
}
