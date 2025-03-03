ac_table = {
    'commands': [
        '--help',
        '--version',
        '--version-full',
        'executor',
        'flow',
        'ping',
        'dryrun',
        'export',
        'new',
        'gateway',
        'hub',
        'auth',
        'help',
        'pod',
        'deployment',
        'client',
    ],
    'completions': {
        'executor': [
            '--help',
            '--name',
            '--workspace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--optout-telemetry',
            '--workspace-id',
            '--extra-search-paths',
            '--timeout-ctrl',
            '--k8s-namespace',
            '--polling',
            '--uses',
            '--uses-with',
            '--uses-metas',
            '--uses-requests',
            '--py-modules',
            '--port-in',
            '--host-in',
            '--native',
            '--output-array-type',
            '--entrypoint',
            '--docker-kwargs',
            '--volumes',
            '--gpus',
            '--disable-auto-volume',
            '--host',
            '--quiet-remote-logs',
            '--upload-files',
            '--runtime-cls',
            '--timeout-ready',
            '--env',
            '--shard-id',
            '--pod-role',
            '--noblock-on-start',
            '--shards',
            '--replicas',
            '--port',
            '--monitoring',
            '--port-monitoring',
            '--retries',
            '--floating',
            '--install-requirements',
            '--force-update',
            '--force',
            '--compression',
            '--uses-before-address',
            '--uses-after-address',
            '--connection-list',
            '--disable-reduce',
            '--timeout-send',
        ],
        'flow': [
            '--help',
            '--name',
            '--workspace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--optout-telemetry',
            '--workspace-id',
            '--uses',
            '--env',
            '--inspect',
        ],
        'ping': ['--help', '--timeout', '--retries'],
        'dryrun': ['--help', '--timeout'],
        'export flowchart': ['--help', '--vertical-layout'],
        'export kubernetes': ['--help', '--k8s-namespace'],
        'export docker-compose': ['--help', '--network_name'],
        'export schema': ['--help', '--yaml-path', '--json-path', '--schema-path'],
        'export': ['--help', 'flowchart', 'kubernetes', 'docker-compose', 'schema'],
        'new': ['--help'],
        'gateway': [
            '--help',
            '--name',
            '--workspace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--optout-telemetry',
            '--workspace-id',
            '--extra-search-paths',
            '--timeout-ctrl',
            '--k8s-namespace',
            '--polling',
            '--uses',
            '--uses-with',
            '--uses-metas',
            '--uses-requests',
            '--py-modules',
            '--port-in',
            '--host-in',
            '--native',
            '--output-array-type',
            '--prefetch',
            '--title',
            '--description',
            '--cors',
            '--no-debug-endpoints',
            '--no-crud-endpoints',
            '--expose-endpoints',
            '--uvicorn-kwargs',
            '--grpc-server-kwargs',
            '--ssl-certfile',
            '--ssl-keyfile',
            '--expose-graphql-endpoint',
            '--protocol',
            '--host',
            '--proxy',
            '--port-expose',
            '--graph-description',
            '--graph-conditions',
            '--deployments-addresses',
            '--deployments-disable-reduce',
            '--compression',
            '--timeout-send',
            '--runtime-cls',
            '--timeout-ready',
            '--env',
            '--shard-id',
            '--pod-role',
            '--noblock-on-start',
            '--shards',
            '--replicas',
            '--port',
            '--monitoring',
            '--port-monitoring',
            '--retries',
            '--floating',
        ],
        'hub new': [
            '--help',
            '--name',
            '--path',
            '--advance-configuration',
            '--description',
            '--keywords',
            '--url',
            '--add-dockerfile',
        ],
        'hub push': [
            '--help',
            '--no-usage',
            '--verbose',
            '--dockerfile',
            '--tag',
            '--protected-tag',
            '--force-update',
            '--force',
            '--build-env',
            '--secret',
            '--no-cache',
            '--public',
            '--private',
        ],
        'hub pull': [
            '--help',
            '--no-usage',
            '--install-requirements',
            '--force-update',
            '--force',
        ],
        'hub': ['--help', 'new', 'push', 'pull'],
        'auth login': ['--help', '--force'],
        'auth logout': ['--help'],
        'auth token create': ['--help', '--expire'],
        'auth token delete': ['--help'],
        'auth token list': ['--help'],
        'auth token': ['--help', 'create', 'delete', 'list'],
        'auth': ['--help', 'login', 'logout', 'token'],
        'help': ['--help'],
        'pod': [
            '--help',
            '--name',
            '--workspace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--optout-telemetry',
            '--workspace-id',
            '--extra-search-paths',
            '--timeout-ctrl',
            '--k8s-namespace',
            '--polling',
            '--uses',
            '--uses-with',
            '--uses-metas',
            '--uses-requests',
            '--py-modules',
            '--port-in',
            '--host-in',
            '--native',
            '--output-array-type',
            '--entrypoint',
            '--docker-kwargs',
            '--volumes',
            '--gpus',
            '--disable-auto-volume',
            '--host',
            '--quiet-remote-logs',
            '--upload-files',
            '--runtime-cls',
            '--timeout-ready',
            '--env',
            '--shard-id',
            '--pod-role',
            '--noblock-on-start',
            '--shards',
            '--replicas',
            '--port',
            '--monitoring',
            '--port-monitoring',
            '--retries',
            '--floating',
            '--install-requirements',
            '--force-update',
            '--force',
            '--compression',
            '--uses-before-address',
            '--uses-after-address',
            '--connection-list',
            '--disable-reduce',
            '--timeout-send',
        ],
        'deployment': [
            '--help',
            '--name',
            '--workspace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--optout-telemetry',
            '--workspace-id',
            '--extra-search-paths',
            '--timeout-ctrl',
            '--k8s-namespace',
            '--polling',
            '--uses',
            '--uses-with',
            '--uses-metas',
            '--uses-requests',
            '--py-modules',
            '--port-in',
            '--host-in',
            '--native',
            '--output-array-type',
            '--entrypoint',
            '--docker-kwargs',
            '--volumes',
            '--gpus',
            '--disable-auto-volume',
            '--host',
            '--quiet-remote-logs',
            '--upload-files',
            '--runtime-cls',
            '--timeout-ready',
            '--env',
            '--shard-id',
            '--pod-role',
            '--noblock-on-start',
            '--shards',
            '--replicas',
            '--port',
            '--monitoring',
            '--retries',
            '--floating',
            '--install-requirements',
            '--force-update',
            '--force',
            '--compression',
            '--uses-before-address',
            '--uses-after-address',
            '--connection-list',
            '--disable-reduce',
            '--timeout-send',
            '--uses-before',
            '--uses-after',
            '--when',
            '--external',
            '--deployment-role',
            '--tls',
            '--port-monitoring',
        ],
        'client': [
            '--help',
            '--host',
            '--proxy',
            '--port',
            '--tls',
            '--asyncio',
            '--return-responses',
            '--protocol',
        ],
    },
}
