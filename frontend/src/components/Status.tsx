import styles from './Status.module.css';

interface ErrorMessageProps {
  message: string;
  onRetry?: () => void;
}

export function ErrorMessage({ message, onRetry }: ErrorMessageProps) {
  return (
    <div className={styles.container}>
      <div className={styles.icon}>!</div>
      <p className={styles.text}>{message}</p>
      {onRetry && (
        <button className={styles.btn} onClick={onRetry}>
          重新加载
        </button>
      )}
    </div>
  );
}

export function EmptyState({ message = '暂无数据' }: { message?: string }) {
  return (
    <div className={styles.container}>
      <div className={styles.emptyIcon}>—</div>
      <p className={styles.text}>{message}</p>
    </div>
  );
}
