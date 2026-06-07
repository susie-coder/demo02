import { useEffect, useRef, useState } from 'react';
import styles from './Hero.module.css';

export default function Hero() {
  const sectionRef = useRef<HTMLElement>(null);
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    // Trigger entrance animation after mount
    requestAnimationFrame(() => setVisible(true));
  }, []);

  const handleCTA = () => {
    const el = document.querySelector('#research');
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <section id="hero" ref={sectionRef} className={styles.hero}>
      <div className={`${styles.content} ${visible ? styles.visible : ''}`}>
        <p className={styles.tag}>Intelligent IoT Laboratory</p>
        <h1 className={styles.title}>
          智能物联网
          <span className={styles.titleAccent}>实验室</span>
        </h1>
        <p className={styles.subtitle}>
          探索边缘智能与物联网的交叉前沿，从感知、通信到认知，<br />
          让每一台设备都拥有智慧的脉搏。
        </p>
        <button className={styles.cta} onClick={handleCTA}>
          探索我们的研究
          <span className={styles.ctaArrow}>→</span>
        </button>
      </div>
      <div className={styles.bgGradient} />
      <div className={styles.bgGrid} />
    </section>
  );
}
