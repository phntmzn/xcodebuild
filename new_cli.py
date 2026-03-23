from pathlib import Path

PROJECT_NAME = "MyCLI"
ORGANIZATION_IDENTIFIER = "com.example"
BUNDLE_ID = f"{ORGANIZATION_IDENTIFIER}.{PROJECT_NAME}"

DESKTOP = Path.home() / "Desktop"
ROOT = DESKTOP / PROJECT_NAME
XCODEPROJ = ROOT / f"{PROJECT_NAME}.xcodeproj"
SOURCES = ROOT / "Sources"

PBXPROJ = f'''// !$*UTF8*$!
{{
	archiveVersion = 1;
	classes = {{
	}};
	objectVersion = 56;
	objects = {{

/* Begin PBXBuildFile section */
		A00000000000000000000011 /* main.swift in Sources */ = {{isa = PBXBuildFile; fileRef = A00000000000000000000001 /* main.swift */; }};
		A00000000000000000000012 /* Foundation.framework in Frameworks */ = {{isa = PBXBuildFile; fileRef = A00000000000000000000021 /* Foundation.framework */; }};
/* End PBXBuildFile section */

/* Begin PBXFileReference section */
		A00000000000000000000001 /* main.swift */ = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = main.swift; sourceTree = "<group>"; }};
		A00000000000000000000021 /* Foundation.framework */ = {{isa = PBXFileReference; lastKnownFileType = wrapper.framework; name = Foundation.framework; path = System/Library/Frameworks/Foundation.framework; sourceTree = SDKROOT; }};
		A00000000000000000000031 /* {PROJECT_NAME} */ = {{isa = PBXFileReference; explicitFileType = "compiled.mach-o.executable"; includeInIndex = 0; path = {PROJECT_NAME}; sourceTree = BUILT_PRODUCTS_DIR; }};
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
		A00000000000000000000041 /* Frameworks */ = {{
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
				A00000000000000000000012 /* Foundation.framework in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
		A00000000000000000000051 = {{
			isa = PBXGroup;
			children = (
				A00000000000000000000052 /* Sources */,
				A00000000000000000000053 /* Frameworks */,
				A00000000000000000000054 /* Products */,
			);
			sourceTree = "<group>";
		}};
		A00000000000000000000052 /* Sources */ = {{
			isa = PBXGroup;
			children = (
				A00000000000000000000001 /* main.swift */,
			);
			path = Sources;
			sourceTree = "<group>";
		}};
		A00000000000000000000053 /* Frameworks */ = {{
			isa = PBXGroup;
			children = (
				A00000000000000000000021 /* Foundation.framework */,
			);
			name = Frameworks;
			sourceTree = "<group>";
		}};
		A00000000000000000000054 /* Products */ = {{
			isa = PBXGroup;
			children = (
				A00000000000000000000031 /* {PROJECT_NAME} */,
			);
			name = Products;
			sourceTree = "<group>";
		}};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
		A00000000000000000000071 /* {PROJECT_NAME} */ = {{
			isa = PBXNativeTarget;
			buildConfigurationList = A00000000000000000000081 /* Build configuration list for PBXNativeTarget "{PROJECT_NAME}" */;
			buildPhases = (
				A00000000000000000000091 /* Sources */,
				A00000000000000000000041 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = {PROJECT_NAME};
			productName = {PROJECT_NAME};
			productReference = A00000000000000000000031 /* {PROJECT_NAME} */;
			productType = "com.apple.product-type.tool";
		}};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
		A00000000000000000000072 /* Project object */ = {{
			isa = PBXProject;
			attributes = {{
				BuildIndependentTargetsInParallel = 1;
				LastSwiftUpdateCheck = 1600;
				LastUpgradeCheck = 1600;
				TargetAttributes = {{
					A00000000000000000000071 = {{
						CreatedOnToolsVersion = 16.0;
					}};
				}};
			}};
			buildConfigurationList = A00000000000000000000082 /* Build configuration list for PBXProject "{PROJECT_NAME}" */;
			compatibilityVersion = "Xcode 14.0";
			developmentRegion = en;
			hasScannedForEncodings = 0;
			knownRegions = (
				en,
				Base,
			);
			mainGroup = A00000000000000000000051;
			productRefGroup = A00000000000000000000054 /* Products */;
			projectDirPath = "";
			projectRoot = "";
			targets = (
				A00000000000000000000071 /* {PROJECT_NAME} */,
			);
		}};
/* End PBXProject section */

/* Begin PBXSourcesBuildPhase section */
		A00000000000000000000091 /* Sources */ = {{
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				A00000000000000000000011 /* main.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
		A00000000000000000000101 /* Debug */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				CODE_SIGN_STYLE = Automatic;
				DEVELOPMENT_TEAM = "";
				GENERATE_INFOPLIST_FILE = YES;
				MACOSX_DEPLOYMENT_TARGET = 13.0;
				PRODUCT_BUNDLE_IDENTIFIER = {BUNDLE_ID};
				PRODUCT_NAME = "$(TARGET_NAME)";
				SDKROOT = macosx;
				SWIFT_VERSION = 5.0;
			}};
			name = Debug;
		}};
		A00000000000000000000102 /* Release */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				CODE_SIGN_STYLE = Automatic;
				DEVELOPMENT_TEAM = "";
				GENERATE_INFOPLIST_FILE = YES;
				MACOSX_DEPLOYMENT_TARGET = 13.0;
				PRODUCT_BUNDLE_IDENTIFIER = {BUNDLE_ID};
				PRODUCT_NAME = "$(TARGET_NAME)";
				SDKROOT = macosx;
				SWIFT_VERSION = 5.0;
			}};
			name = Release;
		}};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
		A00000000000000000000081 /* Build configuration list for PBXNativeTarget "{PROJECT_NAME}" */ = {{
			isa = XCConfigurationList;
			buildConfigurations = (
				A00000000000000000000101 /* Debug */,
				A00000000000000000000102 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		}};
		A00000000000000000000082 /* Build configuration list for PBXProject "{PROJECT_NAME}" */ = {{
			isa = XCConfigurationList;
			buildConfigurations = (
				A00000000000000000000101 /* Debug */,
				A00000000000000000000102 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		}};
/* End XCConfigurationList section */

	}};
	rootObject = A00000000000000000000072 /* Project object */;
}}
'''

MAIN_SWIFT = '''import Foundation

print("Hello from MyCLI")
'''

def main():
    XCODEPROJ.mkdir(parents=True, exist_ok=True)
    SOURCES.mkdir(parents=True, exist_ok=True)

    (XCODEPROJ / "project.pbxproj").write_text(PBXPROJ, encoding="utf-8")
    (SOURCES / "main.swift").write_text(MAIN_SWIFT, encoding="utf-8")

    print(f"Created CLI project at: {ROOT}")
    print(f"Open with: open '{XCODEPROJ}'")

if __name__ == "__main__":
    main()
