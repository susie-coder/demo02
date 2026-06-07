import { useState, useMemo } from 'react';
import { useApi } from '../hooks/useApi';
import type { Paper } from '../types';
import { ErrorMessage, EmptyState } from './Status';
import styles from './Papers.module.css';

export default function Papers() {
  const { data, loading, error, refetch } = useApi<Paper[]>('/api/papers');
  const [expandedId, setExpandedId] = useState<number | null>(null);

  const grouped = useMemo(() => {
    if (!data) return {};
    const groups: Record<number, Paper[]> = {};
    data.forEach((p) => {
      if (!groups[p.year]) groups[p.year] = [];
      groups[p.year].push(p);
    });
    return groups;
  }, [data]);

  const sortedYears = Object.keys(grouped)
    .map(Number)
    .sort((a, b) => b - a);

  return (
    <section id="papers" className={styles.section}>
      <div className={styles.header}>
        <h2 className={styles.title}>论文成果</h2>
        <p className={styles.desc}>
          在顶级期刊和会议上发表的代表性工作
        </p>
      </div>

      {loading && (
        <div style={{ maxWidth: 800, margin: '0 auto', padding: '0 24px' }}>
          {Array.from({ length: 3 }).map((_, i) => (
            <div key={i} style={{ marginBottom: 32 }}>
              <div style={{ width: 60, height: 22, borderRadius: 6, background: '#e8e8ed', marginBottom: 12 }} />
              <div style={{ padding: 20, background: '#fff', borderRadius: 16, border: '1px solid rgba(0,0,0,0.04)' }}>
                <div style={{ width: '70%', height: 18, borderRadius: 4, background: '#e8e8ed', marginBottom: 8 }} />
                <div style={{ width: '40%', height: 14, borderRadius: 4, background: '#e8e8ed' }} />
              </div>
            </div>
          ))}
        </div>
      )}
      {error && <ErrorMessage message={error} onRetry={refetch} />}
      {data && data.length === 0 && <EmptyState message="暂无论文数据" />}

      {data && data.length > 0 && (
        <div className={styles.list}>
          {sortedYears.map((year) => (
            <div key={year} className={styles.yearGroup}>
              <h3 className={styles.year}>{year}</h3>
              {grouped[year].map((paper) => (
                <PaperItem
                  key={paper.id}
                  paper={paper}
                  expanded={expandedId === paper.id}
                  onToggle={() =>
                    setExpandedId(expandedId === paper.id ? null : paper.id)
                  }
                />
              ))}
            </div>
          ))}
        </div>
      )}
    </section>
  );
}

function PaperItem({
  paper,
  expanded,
  onToggle,
}: {
  paper: Paper;
  expanded: boolean;
  onToggle: () => void;
}) {
  return (
    <div className={`${styles.item} ${expanded ? styles.expanded : ''}`}>
      <button className={styles.itemHeader} onClick={onToggle}>
        <div className={styles.itemMain}>
          <span className={styles.itemTitle}>{paper.title}</span>
          <span className={styles.itemMeta}>
            {paper.authors} &middot; <em>{paper.journal}</em>
          </span>
        </div>
        <span className={`${styles.arrow} ${expanded ? styles.arrowUp : ''}`}>
          ▾
        </span>
      </button>
      {expanded && (
        <div className={styles.abstract}>
          <p>{paper.abstract}</p>
          {paper.doi && (
            <a
              className={styles.doi}
              href={`https://doi.org/${paper.doi}`}
              target="_blank"
              rel="noopener noreferrer"
            >
              DOI: {paper.doi}
            </a>
          )}
        </div>
      )}
    </div>
  );
}
