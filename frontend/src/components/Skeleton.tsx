import styles from './Skeleton.module.css';

interface SkeletonProps {
  type?: 'card' | 'list' | 'hero' | 'text';
  count?: number;
}

export default function Skeleton({ type = 'card', count = 3 }: SkeletonProps) {
  if (type === 'hero') {
    return (
      <div className={styles.hero}>
        <div className={`${styles.pulse} ${styles.heroTitle}`} />
        <div className={`${styles.pulse} ${styles.heroSubtitle}`} />
        <div className={`${styles.pulse} ${styles.heroBtn}`} />
      </div>
    );
  }

  if (type === 'text') {
    return (
      <div className={styles.textBlock}>
        {Array.from({ length: count }).map((_, i) => (
          <div key={i} className={`${styles.pulse} ${styles.textLine}`} style={{ width: `${80 - i * 10}%` }} />
        ))}
      </div>
    );
  }

  return (
    <div className={type === 'card' ? styles.cardGrid : styles.listContainer}>
      {Array.from({ length: count }).map((_, i) => (
        <div key={i} className={type === 'card' ? styles.card : styles.listItem}>
          {type === 'card' ? (
            <>
              <div className={`${styles.pulse} ${styles.cardIcon}`} />
              <div className={`${styles.pulse} ${styles.cardTitle}`} />
              <div className={`${styles.pulse} ${styles.cardDesc}`} />
              <div className={`${styles.pulse} ${styles.cardDesc}`} style={{ width: '60%' }} />
            </>
          ) : (
            <>
              <div className={`${styles.pulse} ${styles.listAvatar}`} />
              <div className={styles.listContent}>
                <div className={`${styles.pulse} ${styles.listTitle}`} />
                <div className={`${styles.pulse} ${styles.listSub}`} />
              </div>
            </>
          )}
        </div>
      ))}
    </div>
  );
}
