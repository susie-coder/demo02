import { useApi } from '../hooks/useApi';
import type { ResearchArea } from '../types';
import Skeleton from './Skeleton';
import { ErrorMessage, EmptyState } from './Status';
import styles from './Research.module.css';

export default function Research() {
  const { data, loading, error, refetch } = useApi<ResearchArea[]>('/api/research');

  return (
    <section id="research" className={styles.section}>
      <div className={styles.header}>
        <h2 className={styles.title}>研究方向</h2>
        <p className={styles.desc}>
          在边缘计算、物联网通信、联邦学习等前沿领域持续探索
        </p>
      </div>

      {loading && <Skeleton type="card" count={6} />}
      {error && <ErrorMessage message={error} onRetry={refetch} />}
      {data && data.length === 0 && <EmptyState message="暂无研究方向数据" />}

      {data && data.length > 0 && (
        <div className={styles.grid}>
          {data.map((area) => (
            <ResearchCard key={area.id} area={area} />
          ))}
        </div>
      )}
    </section>
  );
}

function ResearchCard({ area }: { area: ResearchArea }) {
  return (
    <div className={styles.card}>
      <div className={styles.icon}>{area.icon || '🔬'}</div>
      <h3 className={styles.cardTitle}>{area.name}</h3>
      <p className={styles.cardDesc}>{area.description}</p>
    </div>
  );
}
