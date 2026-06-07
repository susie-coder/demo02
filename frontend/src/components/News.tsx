import { useState } from 'react';
import { useApi } from '../hooks/useApi';
import type { NewsItem } from '../types';
import Skeleton from './Skeleton';
import { ErrorMessage, EmptyState } from './Status';
import styles from './News.module.css';

export default function News() {
  const { data, loading, error, refetch } = useApi<NewsItem[]>('/api/news');
  const [expandedId, setExpandedId] = useState<number | null>(null);

  return (
    <section id="news" className={styles.section}>
      <div className={styles.header}>
        <h2 className={styles.title}>新闻动态</h2>
        <p className={styles.desc}>
          实验室最新成果、荣誉与活动资讯
        </p>
      </div>

      {loading && <Skeleton type="text" count={5} />}
      {error && <ErrorMessage message={error} onRetry={refetch} />}
      {data && data.length === 0 && <EmptyState message="暂无新闻动态" />}

      {data && data.length > 0 && (
        <div className={styles.timeline}>
          {data.map((item) => (
            <NewsItemCard
              key={item.id}
              item={item}
              expanded={expandedId === item.id}
              onToggle={() =>
                setExpandedId(expandedId === item.id ? null : item.id)
              }
            />
          ))}
        </div>
      )}
    </section>
  );
}

function NewsItemCard({
  item,
  expanded,
  onToggle,
}: {
  item: NewsItem;
  expanded: boolean;
  onToggle: () => void;
}) {
  return (
    <div className={`${styles.card} ${expanded ? styles.expanded : ''}`}>
      <div className={styles.dot} />
      <div className={styles.cardBody}>
        <span className={styles.date}>{item.date}</span>
        <h3 className={styles.cardTitle}>{item.title}</h3>
        <p className={styles.summary}>{item.summary}</p>
        {expanded && (
          <div className={styles.content}>
            <p>{item.content}</p>
          </div>
        )}
        <button className={styles.toggle} onClick={onToggle}>
          {expanded ? '收起' : '阅读全文'}
        </button>
      </div>
    </div>
  );
}
