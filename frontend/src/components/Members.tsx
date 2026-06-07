import { useApi } from '../hooks/useApi';
import type { Member } from '../types';
import Skeleton from './Skeleton';
import { ErrorMessage, EmptyState } from './Status';
import styles from './Members.module.css';

export default function Members() {
  const { data, loading, error, refetch } = useApi<Member[]>('/api/members');

  return (
    <section id="members" className={styles.section}>
      <div className={styles.header}>
        <h2 className={styles.title}>团队成员</h2>
        <p className={styles.desc}>
          汇聚物联网与边缘智能领域的优秀研究者
        </p>
      </div>

      {loading && <Skeleton type="list" count={4} />}
      {error && <ErrorMessage message={error} onRetry={refetch} />}
      {data && data.length === 0 && <EmptyState message="暂无团队成员数据" />}

      {data && data.length > 0 && (
        <div className={styles.grid}>
          {data.map((m) => (
            <MemberCard key={m.id} member={m} />
          ))}
        </div>
      )}
    </section>
  );
}

function MemberCard({ member }: { member: Member }) {
  return (
    <div className={styles.card}>
      <img
        className={styles.avatar}
        src={member.avatar || `https://api.dicebear.com/9.x/initials/svg?seed=${encodeURIComponent(member.name)}`}
        alt={member.name}
        loading="lazy"
      />
      <div className={styles.info}>
        <h3 className={styles.name}>{member.name}</h3>
        <p className={styles.role}>{member.role}</p>
        <p className={styles.bio}>{member.bio}</p>
        {member.email && (
          <a className={styles.email} href={`mailto:${member.email}`}>
            {member.email}
          </a>
        )}
      </div>
    </div>
  );
}
