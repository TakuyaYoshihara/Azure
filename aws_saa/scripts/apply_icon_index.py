#!/usr/bin/env python3
"""案B: 章頭のサービス一覧表にアイコンを集約し、見出し下の単独アイコンを削除する。"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ICON_W = 32
INDEX_HEADING = "### 本章のサービス一覧\n"
IMG_LINE_RE = re.compile(
    r'\n<img src="images/aws-icons/[^"]+" alt="[^"]*"(?: width="48")?/>\n',
)

# (icon file, display name, one-liner) — 章の登場順
CHAPTER_SERVICES: dict[str, list[tuple[str, str, str]]] = {
    "saa_computing.ipynb": [
        ("ec2.png", "Amazon EC2", "仮想サーバー（VM）"),
        ("autoscaling.png", "Amazon EC2 Auto Scaling", "需要に応じてEC2台数を自動調整"),
        ("batch.png", "AWS Batch", "大量ジョブのバッチ実行"),
        ("lambda.png", "AWS Lambda", "イベント駆動のサーバーレス実行"),
        ("apigateway.png", "Amazon API Gateway", "HTTP/WebSocket APIの入口"),
        ("fargate.png", "AWS Fargate", "サーバーレスでコンテナ実行"),
        (
            "serverless-application-repository.png",
            "AWS Serverless Application Repository",
            "サーバーレスアプリのテンプレートカタログ",
        ),
        ("outposts.png", "AWS Outposts", "オンプレにAWSインフラを設置"),
        ("vmware-cloud.png", "VMware Cloud on AWS", "vSphere環境をAWS上で運用"),
        ("wavelength.png", "AWS Wavelength", "5Gエッジで超低遅延コンピュート"),
    ],
    "saa_storage.ipynb": [
        ("ebs.png", "Amazon EBS", "EC2用ブロックディスク"),
        ("efs.png", "Amazon EFS", "Linux向け共有ファイル（NFS）"),
        ("s3.png", "Amazon S3", "オブジェクトストレージ"),
        ("storage-gateway.png", "AWS Storage Gateway", "オンプレとクラウドストレージの橋"),
        ("data-sync.png", "AWS DataSync", "オンプレ↔AWSのオンライン同期"),
        ("snowball.png", "AWS Snowball", "大容量データのオフライン搬送"),
        ("aws-backup.png", "AWS Backup", "複数サービスのバックアップ一元管理"),
        ("fsx.png", "Amazon FSx", "Windows/Lustre等の高性能ファイル"),
    ],
    "saa_security.ipynb": [
        ("iam.png", "AWS IAM", "リソースへのアクセス制御"),
        ("iam-identity-center.png", "AWS IAM Identity Center", "社内SSO・複数アカウントログイン"),
        ("directory-service.png", "AWS Directory Service", "マネージドAD（オンプレAD連携）"),
        ("cognito.png", "Amazon Cognito", "アプリ向けユーザー認証"),
        ("artifact.png", "AWS Artifact", "コンプライアンス報告書の入手"),
        ("audit-manager.png", "AWS Audit Manager", "監査証跡の継続的収集"),
        ("detective.png", "Amazon Detective", "セキュリティ調査の分析基盤"),
        ("security-hub.png", "AWS Security Hub", "複数ツールの findings を集約"),
        ("guardduty.png", "Amazon GuardDuty", "脅威検知（ログ分析）"),
        ("macie.png", "Amazon Macie", "S3の機密データ検出"),
        ("inspector.png", "Amazon Inspector", "脆弱性スキャン"),
        ("config.png", "AWS Config", "リソース設定の評価・コンプライアンス"),
        ("cloudtrail.png", "AWS CloudTrail", "API操作の監査ログ"),
        ("kms.png", "AWS KMS", "暗号鍵の作成・管理"),
        ("acm.png", "AWS Certificate Manager", "TLS証明書の発行・更新"),
        ("secrets-manager.png", "AWS Secrets Manager", "APIキー等のシークレット管理"),
        ("cloudhsm.png", "AWS CloudHSM", "専用HSMによる鍵管理"),
        ("firewall-manager.png", "AWS Firewall Manager", "WAF等を組織横断で配布"),
        ("network-firewall.png", "AWS Network Firewall", "VPC内のL3〜L7ファイアウォール"),
        ("shield.png", "AWS Shield", "DDoS防御（Standard/Advanced）"),
        ("waf.png", "AWS WAF", "HTTP/HTTPS向けWeb攻撃防御"),
    ],
    "saa_network.ipynb": [
        ("vpc.png", "Amazon VPC", "論理的に隔離した仮想ネットワーク"),
        ("nat-gateway.png", "NAT Gateway", "プライベートサブネットから外向き通信"),
        ("route53.png", "Amazon Route 53", "DNS・ヘルスチェック・ルーティング"),
        ("elb.png", "Elastic Load Balancing", "トラフィック分散（ALB/NLB）"),
        ("cloudfront.png", "Amazon CloudFront", "コンテンツのキャッシュ配信（CDN）"),
        ("global-accelerator.png", "AWS Global Accelerator", "グローバル経路最適化・固定IP"),
        ("private-link.png", "AWS PrivateLink", "VPCからサービスへプライベート接続"),
        ("transit-gateway.png", "AWS Transit Gateway", "多数VPCをハブで接続"),
    ],
    "saa_governance.ipynb": [
        ("organizations.png", "AWS Organizations", "複数AWSアカウントの一元管理"),
        ("control-tower.png", "AWS Control Tower", "マルチアカウントのランディングゾーン"),
        ("cloudwatch.png", "Amazon CloudWatch", "メトリクス・ログ・アラーム"),
        ("systems-manager.png", "AWS Systems Manager", "パッチ・Run Command等の運用"),
        ("trusted-advisor.png", "AWS Trusted Advisor", "ベストプラクティス提案"),
        ("compute-optimizer.png", "AWS Compute Optimizer", "リソースのライトサイジング提案"),
        (
            "managed-grafana.png",
            "Amazon Managed Grafana / Prometheus",
            "マネージドな可観測性スタック",
        ),
        ("eventbridge.png", "Amazon EventBridge", "イベント駆動の連携・自動化"),
        ("config.png", "AWS Config", "リソース設定の評価・コンプライアンス"),
        ("cloudtrail.png", "AWS CloudTrail", "API操作の監査ログ"),
        ("cost-explorer.png", "AWS Cost Explorer", "コストの分析・可視化"),
        ("budgets.png", "AWS Budgets", "予算超過のアラート"),
        ("well-architected-tool.png", "AWS Well-Architected Tool", "設計レビューの枠組み"),
        ("service-catalog.png", "AWS Service Catalog", "承認済み製品のカタログ配布"),
    ],
    "saa_database.ipynb": [
        ("rds.png", "Amazon RDS", "マネージドSQL（MySQL等）"),
        ("aurora.png", "Amazon Aurora", "高可用・高性能RDB（MySQL/PostgreSQL互換）"),
        ("rds-proxy.png", "Amazon RDS Proxy", "DB接続プールで接続枯渇を緩和"),
        ("dynamodb.png", "Amazon DynamoDB", "スケールするNoSQL（キー・バリュー）"),
        ("dynamodb-dax.png", "DynamoDB Accelerator (DAX)", "DynamoDB専用の読取キャッシュ"),
        ("documentdb.png", "Amazon DocumentDB", "MongoDB互換ドキュメントDB"),
        ("keyspaces.png", "Amazon Keyspaces", "Cassandra互換のワイドカラムDB"),
        ("elasticache.png", "Amazon ElastiCache", "Redis/Memcachedのインメモリキャッシュ"),
        ("neptune.png", "Amazon Neptune", "グラフDB（関係性データ）"),
        ("database.png", "Amazon QLDB", "改ざん不能な台帳・監査"),
        ("redshift.png", "Amazon Redshift", "データウェアハウス（OLAP）"),
        ("athena.png", "Amazon Athena", "S3上のデータにSQLクエリ"),
        ("glue.png", "AWS Glue", "ETLとデータカタログ"),
    ],
}

# 挿入位置: (正規表現, 置換) — 構成リストの直後に一覧を入れる
INSERT_AFTER: dict[str, tuple[str, str]] = {
    "saa_computing.ipynb": (
        r"(- エッジコンピューティング\n)\n",
        r"\1\n" + INDEX_HEADING + "\n",
    ),
    "saa_storage.ipynb": (
        r"(- 高性能ファイルシステム\n)\n",
        r"\1\n" + INDEX_HEADING + "\n",
    ),
    "saa_security.ipynb": (
        r"(- ネットワークセキュリティ\n)\n",
        r"\1\n" + INDEX_HEADING + "\n",
    ),
    "saa_network.ipynb": (
        r"(- AWS PrivateLink\n)\n",
        r"\1\n" + INDEX_HEADING + "\n",
    ),
    "saa_governance.ipynb": (
        r"(- コスト管理と最適化\n)\n",
        r"\1\n" + INDEX_HEADING + "\n",
    ),
    "saa_database.ipynb": (
        r"(- コスト最適化とキャパシティプランニング\n)\n",
        r"\1\n" + INDEX_HEADING + "\n",
    ),
}


def build_table(services: list[tuple[str, str, str]]) -> str:
    rows = [
        "| | サービス | ひとこと |",
        "|---|----------|----------|",
    ]
    for icon, name, desc in services:
        rows.append(
            f'| <img src="images/aws-icons/{icon}" width="{ICON_W}" alt="{name}"/> '
            f"| **{name}** | {desc} |"
        )
    return "\n".join(rows) + "\n\n"


def strip_standalone_icons(text: str) -> str:
    prev = None
    while prev != text:
        prev = text
        text = IMG_LINE_RE.sub("\n", text)
    # 連続する空行を最大2つに
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    # 見出し直後の余分な空行を1つに
    text = re.sub(r"(#{1,3} [^\n]+\n)\n\n+([^#\n|>])", r"\1\n\n\2", text)
    return text


def apply_notebook(nb_name: str) -> None:
    path = ROOT / nb_name
    data = json.loads(path.read_text(encoding="utf-8"))
    text = "".join(data["cells"][0]["source"])

    text = strip_standalone_icons(text)

    if INDEX_HEADING not in text:
        services = CHAPTER_SERVICES[nb_name]
        table = build_table(services)
        pattern, repl = INSERT_AFTER[nb_name]
        new_text, n = re.subn(pattern, repl + table, text, count=1)
        if n != 1:
            raise RuntimeError(f"{nb_name}: insert anchor not found")
        text = new_text
    elif "images/aws-icons/" in text and '<img src="images/aws-icons/' in text:
        # 一覧はあるが本文に残存アイコン → strip only
        pass

    if re.search(r'\n<img src="images/aws-icons/', text):
        # 一覧表内以外に残っていないか（一覧は | <img で始まる）
        body_icons = re.findall(
            r'<img src="images/aws-icons/[^"]+" width="48"',
            text,
        )
        if body_icons:
            raise RuntimeError(f"{nb_name}: standalone 48px icons remain: {len(body_icons)}")

    data["cells"][0]["source"] = [
        line if line.endswith("\n") else line + "\n"
        for line in text.splitlines(True)
    ]
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"  OK {nb_name}")


def main() -> None:
    order = [
        "saa_computing.ipynb",
        "saa_storage.ipynb",
        "saa_security.ipynb",
        "saa_network.ipynb",
        "saa_governance.ipynb",
        "saa_database.ipynb",
    ]
    for nb in order:
        apply_notebook(nb)
    print("Done.")


if __name__ == "__main__":
    main()
