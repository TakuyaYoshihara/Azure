#!/usr/bin/env python3
"""Download AWS Architecture Icons for SAA notebooks."""
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ICON_DIR = ROOT / "images" / "aws-icons"
BASE = "https://raw.githubusercontent.com/awslabs/aws-icons-for-plantuml/v23.0"

# Official AWS Architecture Icons (via AWS Labs PlantUML distribution v23.0)
ICONS = {
    "ec2.png": f"{BASE}/dist/Compute/EC2.png",
    "autoscaling.png": f"{BASE}/dist/Compute/EC2AutoScaling.png",
    "batch.png": f"{BASE}/dist/Compute/Batch.png",
    "lambda.png": f"{BASE}/dist/Compute/Lambda.png",
    "apigateway.png": f"{BASE}/dist/NetworkingContentDelivery/APIGateway.png",
    "fargate.png": f"{BASE}/dist/Containers/Fargate.png",
    "serverless-application-repository.png": f"{BASE}/dist/Compute/ServerlessApplicationRepository.png",
    "outposts.png": f"{BASE}/dist/Compute/Outpostsfamily.png",
    "vmware-cloud.png": f"{BASE}/dist/Compute/ElasticVMwareService.png",
    "wavelength.png": f"{BASE}/dist/Compute/Wavelength.png",
    "ebs.png": f"{BASE}/dist/Storage/ElasticBlockStore.png",
    "efs.png": f"{BASE}/dist/Storage/EFS.png",
    "s3.png": f"{BASE}/dist/Storage/SimpleStorageService.png",
    "storage-gateway.png": f"{BASE}/dist/Storage/StorageGateway.png",
    "fsx.png": f"{BASE}/dist/Storage/FSx.png",
    "elb.png": f"{BASE}/dist/NetworkingContentDelivery/ElasticLoadBalancing.png",
    "global-accelerator.png": f"{BASE}/dist/NetworkingContentDelivery/GlobalAccelerator.png",
    "private-link.png": f"{BASE}/dist/NetworkingContentDelivery/PrivateLink.png",
    "cloudfront.png": f"{BASE}/dist/NetworkingContentDelivery/CloudFront.png",
    "vpc.png": f"{BASE}/dist/Groups/VPC.png",
    "nat-gateway.png": f"{BASE}/dist/NetworkingContentDelivery/VPCNATGateway.png",
    "route53.png": f"{BASE}/dist/NetworkingContentDelivery/Route53.png",
    "iam.png": f"{BASE}/dist/SecurityIdentityCompliance/IdentityAccessManagementPermissions.png",
    "iam-identity-center.png": f"{BASE}/dist/SecurityIdentityCompliance/IAMIdentityCenter.png",
    "directory-service.png": f"{BASE}/dist/SecurityIdentityCompliance/DirectoryService.png",
    "cognito.png": f"{BASE}/dist/SecurityIdentityCompliance/Cognito.png",
    "artifact.png": f"{BASE}/dist/SecurityIdentityCompliance/Artifact.png",
    "audit-manager.png": f"{BASE}/dist/SecurityIdentityCompliance/AuditManager.png",
    "detective.png": f"{BASE}/dist/SecurityIdentityCompliance/Detective.png",
    "security-hub.png": f"{BASE}/dist/SecurityIdentityCompliance/SecurityHub.png",
    "guardduty.png": f"{BASE}/dist/SecurityIdentityCompliance/GuardDuty.png",
    "macie.png": f"{BASE}/dist/SecurityIdentityCompliance/Macie.png",
    "inspector.png": f"{BASE}/dist/SecurityIdentityCompliance/Inspector.png",
    "config.png": f"{BASE}/dist/ManagementGovernance/Config.png",
    "cloudtrail.png": f"{BASE}/dist/ManagementGovernance/CloudTrail.png",
    "kms.png": f"{BASE}/dist/SecurityIdentityCompliance/KeyManagementService.png",
    "acm.png": f"{BASE}/dist/SecurityIdentityCompliance/CertificateManager.png",
    "secrets-manager.png": f"{BASE}/dist/SecurityIdentityCompliance/SecretsManager.png",
    "cloudhsm.png": f"{BASE}/dist/SecurityIdentityCompliance/CloudHSM.png",
    "firewall-manager.png": f"{BASE}/dist/SecurityIdentityCompliance/FirewallManager.png",
    "network-firewall.png": f"{BASE}/dist/SecurityIdentityCompliance/NetworkFirewall.png",
    "shield.png": f"{BASE}/dist/SecurityIdentityCompliance/Shield.png",
    "waf.png": f"{BASE}/dist/SecurityIdentityCompliance/WAF.png",
    "organizations.png": f"{BASE}/dist/ManagementGovernance/Organizations.png",
    "control-tower.png": f"{BASE}/dist/ManagementGovernance/ControlTower.png",
    "cloudwatch.png": f"{BASE}/dist/ManagementGovernance/CloudWatch.png",
    "systems-manager.png": f"{BASE}/dist/ManagementGovernance/SystemsManager.png",
    "trusted-advisor.png": f"{BASE}/dist/ManagementGovernance/TrustedAdvisor.png",
    "compute-optimizer.png": f"{BASE}/dist/ManagementGovernance/ComputeOptimizer.png",
    "managed-grafana.png": f"{BASE}/dist/ManagementGovernance/ManagedGrafana.png",
    "eventbridge.png": f"{BASE}/dist/ApplicationIntegration/EventBridge.png",
    "cost-explorer.png": f"{BASE}/dist/CloudFinancialManagement/CostExplorer.png",
    "budgets.png": f"{BASE}/dist/CloudFinancialManagement/Budgets.png",
    "well-architected-tool.png": f"{BASE}/dist/ManagementGovernance/WellArchitectedTool.png",
    "service-catalog.png": f"{BASE}/dist/ManagementGovernance/ServiceCatalog.png",
    "rds.png": f"{BASE}/dist/Database/RDS.png",
    "aurora.png": f"{BASE}/dist/Database/Aurora.png",
    "dynamodb.png": f"{BASE}/dist/Database/DynamoDB.png",
    "documentdb.png": f"{BASE}/dist/Database/DocumentDB.png",
    "keyspaces.png": f"{BASE}/dist/Database/Keyspaces.png",
    "elasticache.png": f"{BASE}/dist/Database/ElastiCache.png",
    "neptune.png": f"{BASE}/dist/Database/Neptune.png",
    "database.png": f"{BASE}/dist/Database/Database.png",
    "redshift.png": f"{BASE}/dist/Analytics/Redshift.png",
    "athena.png": f"{BASE}/dist/Analytics/Athena.png",
    "glue.png": f"{BASE}/dist/Analytics/Glue.png",
    "rds-proxy.png": f"{BASE}/dist/Database/RDSProxyInstance.png",
    "dynamodb-dax.png": f"{BASE}/dist/Database/DynamoDBAmazonDynamoDBAccelerator.png",
    "data-sync.png": f"{BASE}/dist/MigrationModernization/DataSync.png",
    "snowball.png": f"{BASE}/dist/Storage/Snowball.png",
    "aws-backup.png": f"{BASE}/dist/Storage/Backup.png",
    "transit-gateway.png": f"{BASE}/dist/NetworkingContentDelivery/TransitGateway.png",
}

def download_icons():
    ICON_DIR.mkdir(parents=True, exist_ok=True)
    for name, url in ICONS.items():
        dest = ICON_DIR / name
        if dest.exists() and dest.stat().st_size > 0:
            continue
        print(f"Downloading {name}...")
        urllib.request.urlretrieve(url, dest)


def write_readme():
    readme = ICON_DIR / "README.md"
    readme.write_text(
        """# AWS Architecture Icons

These PNG icons are from the [AWS Architecture Icons](https://aws.amazon.com/architecture/icons/) set,
distributed via [awslabs/aws-icons-for-plantuml](https://github.com/awslabs/aws-icons-for-plantuml) release **v23.0**.

Use follows AWS guidance for architecture diagrams and educational materials.
Do not modify icons in ways that misrepresent AWS services.

Source: https://github.com/awslabs/aws-icons-for-plantuml/tree/v23.0/dist
""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    download_icons()
    write_readme()
    print("Icons downloaded. Run: python3 scripts/apply_icon_index.py")
