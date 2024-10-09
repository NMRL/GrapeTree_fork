# Server Socket
bind = '0.0.0.0:8000'

# Worker Processes
workers = 4  # Adjust based on your application's load and CPU count
threads = 2  # Number of threads per worker

# Logging
accesslog = '-'  # Log access to stdout
errorlog = '-'  # Log errors to stdout
loglevel = 'info'

# Security
# worker_tmp_dir = '/dev/shm'  # Uncomment if using a tmpfs mount for security/performance

# Performance
timeout = 30  # Timeout for worker processes
keepalive = 2  # Keep-alive for connections