from pathlib import Path

PROJECT_NAME = "MyCocoaFramework"
ORGANIZATION_IDENTIFIER = "com.example"
BUNDLE_ID = f"{ORGANIZATION_IDENTIFIER}.{PROJECT_NAME}"

DESKTOP = Path.home() / "Desktop"
ROOT = DESKTOP / PROJECT_NAME
XCODEPROJ = ROOT / f"{PROJECT_NAME}.xcodeproj"
SOURCES = ROOT / "Sources"
HEADERS = ROOT / "Headers"

PBXPROJ = f'''// !$*UTF8*$!
{{
	archiveVersion = 1;
	classes = {{
	}};
	objectVersion = 56;
	objects = {{

/* Begin PBXBuildFile section */
		A00000000000000000000011 /* {PROJECT_NAME}.swift in Sources */ = {{isa = PBXBuildFile; fileRef = A00000000000000000000001 /* {PROJECT_NAME}.swift */; }};
		A00000000000000000000012 /* AppKit.framework in Frameworks */ = {{isa = PBXBuildFile; fileRef = A00000000000000000000021 /* AppKit.framework */; }};
		A00000000000000000000013 /* Foundation.framework in Frameworks */ = {{isa = PBXBuildFile; fileRef = A00000000000000000000022 /* Foundation.framework */; }};
		A00000000000000000000014 /* {PROJECT_NAME}.h in Headers */ = {{isa = PBXBuildFile; fileRef = A00000000000000000000002 /* {PROJECT_NAME}.h */; settings = {{ATTRIBUTES = (Public, ); }}; }};
/* End PBXBuildFile section */

/* Begin PBXFileReference section */
		A00000000000000000000001 /* {PROJECT_NAME}.swift */ = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = {PROJECT_NAME}.swift; sourceTree = "<group>"; }};
		A00000000000000000000002 /* {PROJECT_NAME}.h */ = {{isa = PBXFileReference; lastKnownFileType = sourcecode.c.h; path = {PROJECT_NAME}.h; sourceTree = "<group>"; }};
		A00000000000000000000021 /* AppKit.framework */ = {{isa = PBXFileReference; lastKnownFileType = wrapper.framework; name = AppKit.framework; path = System/Library/Frameworks/AppKit.framework; sourceTree = SDKROOT; }};
		A00000000000000000000022 /* Foundation.framework */ = {{isa = PBXFileReference; lastKnownFileType = wrapper.framework; name = Foundation.framework; path = System/Library/Frameworks/Foundation.framework; sourceTree = SDKROOT; }};
		A00000000000000000000031 /* {PROJECT_NAME}.framework */ = {{isa = PBXFileReference; explicitFileType = wrapper.framework; includeInIndex = 0; path = {PROJECT_NAME}.framework; sourceTree = BUILT_PRODUCTS_DIR; }};
		A00000000000000000000032 /* Info.plist */ = {{isa = PBXFileReference; lastKnownFileType = text.plist.xml; path = Info.plist; sourceTree = "<group>"; }};
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
		A00000000000000000000041 /* Frameworks */ = {{
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
				A00000000000000000000012 /* AppKit.framework in Frameworks */,
				A00000000000000000000013 /* Foundation.framework in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
		A00000000000000000000051 = {{
			isa = PBXGroup;
			children = (
				A00000000000000000000052 /* Sources */,
				A00000000000000000000055 /* Headers */,
				A00000000000000000000053 /* Frameworks */,
				A00000000000000000000054 /* Products */,
				A00000000000000000000032 /* Info.plist */,
			);
			sourceTree = "<group>";
		}};
		A00000000000000000000052 /* Sources */ = {{
			isa = PBXGroup;
			children = (
				A00000000000000000000001 /* {PROJECT_NAME}.swift */,
			);
			path = Sources;
			sourceTree = "<group>";
		}};
		A00000000000000000000055 /* Headers */ = {{
			isa = PBXGroup;
			children = (
				A00000000000000000000002 /* {PROJECT_NAME}.h */,
			);
			path = Headers;
			sourceTree = "<group>";
		}};
		A00000000000000000000053 /* Frameworks */ = {{
			isa = PBXGroup;
			children = (
				A00000000000000000000021 /* AppKit.framework */,
				A00000000000000000000022 /* Foundation.framework */,
			);
			name = Frameworks;
			sourceTree = "<group>";
		}};
		A00000000000000000000054 /* Products */ = {{
			isa = PBXGroup;
			children = (
				A00000000000000000000031 /* {PROJECT_NAME}.framework */,
			);
			name = Products;
			sourceTree = "<group>";
		}};
/* End PBXGroup section */

/* Begin PBXHeadersBuildPhase section */
		A00000000000000000000061 /* Headers */ = {{
			isa = PBXHeadersBuildPhase;
			buildActionMask = 2147483647;
			files = (
				A00000000000000000000014 /* {PROJECT_NAME}.h in Headers */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXHeadersBuildPhase section */

/* Begin PBXNativeTarget section */
		A00000000000000000000071 /* {PROJECT_NAME} */ = {{
			isa = PBXNativeTarget;
			buildConfigurationList = A00000000000000000000081 /* Build configuration list for PBXNativeTarget "{PROJECT_NAME}" */;
			buildPhases = (
				A00000000000000000000091 /* Sources */,
				A00000000000000000000061 /* Headers */,
				A00000000000000000000041 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = {PROJECT_NAME};
			productName = {PROJECT_NAME};
			productReference = A00000000000000000000031 /* {PROJECT_NAME}.framework */;
			productType = "com.apple.product-type.framework";
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
				A00000000000000000000011 /* {PROJECT_NAME}.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
		A00000000000000000000101 /* Debug */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				CLANG_ENABLE_MODULES = YES;
				CODE_SIGN_STYLE = Automatic;
				CURRENT_PROJECT_VERSION = 1;
				DEFINES_MODULE = YES;
				DYLIB_COMPATIBILITY_VERSION = 1;
				DYLIB_CURRENT_VERSION = 1;
				INFOPLIST_FILE = Info.plist;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/../Frameworks",
					"@loader_path/../Frameworks",
					"@loader_path/Frameworks",
				);
				MACOSX_DEPLOYMENT_TARGET = 13.0;
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = {BUNDLE_ID};
				PRODUCT_MODULE_NAME = {PROJECT_NAME};
				PRODUCT_NAME = "$(TARGET_NAME)";
				PUBLIC_HEADERS_FOLDER_PATH = "$(CONTENTS_FOLDER_PATH)/Headers";
				SDKROOT = macosx;
				SKIP_INSTALL = YES;
				SUPPORTED_PLATFORMS = macosx;
				SWIFT_INSTALL_OBJC_HEADER = YES;
				SWIFT_OBJC_INTERFACE_HEADER_NAME = {PROJECT_NAME}-Swift.h;
				SWIFT_VERSION = 5.0;
				WRAPPER_EXTENSION = framework;
			}};
			name = Debug;
		}};
		A00000000000000000000102 /* Release */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				CLANG_ENABLE_MODULES = YES;
				CODE_SIGN_STYLE = Automatic;
				CURRENT_PROJECT_VERSION = 1;
				DEFINES_MODULE = YES;
				DYLIB_COMPATIBILITY_VERSION = 1;
				DYLIB_CURRENT_VERSION = 1;
				INFOPLIST_FILE = Info.plist;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/../Frameworks",
					"@loader_path/../Frameworks",
					"@loader_path/Frameworks",
				);
				MACOSX_DEPLOYMENT_TARGET = 13.0;
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = {BUNDLE_ID};
				PRODUCT_MODULE_NAME = {PROJECT_NAME};
				PRODUCT_NAME = "$(TARGET_NAME)";
				PUBLIC_HEADERS_FOLDER_PATH = "$(CONTENTS_FOLDER_PATH)/Headers";
				SDKROOT = macosx;
				SKIP_INSTALL = YES;
				SUPPORTED_PLATFORMS = macosx;
				SWIFT_INSTALL_OBJC_HEADER = YES;
				SWIFT_OBJC_INTERFACE_HEADER_NAME = {PROJECT_NAME}-Swift.h;
				SWIFT_VERSION = 5.0;
				WRAPPER_EXTENSION = framework;
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

SWIFT_FILE = f'''import AppKit
import Foundation

@objcMembers
public final class {PROJECT_NAME}API: NSObject {{
    public override init() {{
        super.init()
    }}

    public func hello() -> String {{
        "Hello from {PROJECT_NAME}"
    }}
}}
'''

HEADER_FILE = f'''#import <Foundation/Foundation.h>

//! Project version number for {PROJECT_NAME}.
FOUNDATION_EXPORT double {PROJECT_NAME}VersionNumber;

//! Project version string for {PROJECT_NAME}.
FOUNDATION_EXPORT const unsigned char {PROJECT_NAME}VersionString[];
'''

INFO_PLIST = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CFBundleDevelopmentRegion</key>
	<string>$(DEVELOPMENT_LANGUAGE)</string>
	<key>CFBundleExecutable</key>
	<string>$(EXECUTABLE_NAME)</string>
	<key>CFBundleIdentifier</key>
	<string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
	<key>CFBundleInfoDictionaryVersion</key>
	<string>6.0</string>
	<key>CFBundleName</key>
	<string>$(PRODUCT_NAME)</string>
	<key>CFBundlePackageType</key>
	<string>FMWK</string>
	<key>CFBundleShortVersionString</key>
	<string>$(MARKETING_VERSION)</string>
	<key>CFBundleVersion</key>
	<string>$(CURRENT_PROJECT_VERSION)</string>
	<key>NSPrincipalClass</key>
	<string></string>
</dict>
</plist>
'''

def main():
    XCODEPROJ.mkdir(parents=True, exist_ok=True)
    SOURCES.mkdir(parents=True, exist_ok=True)
    HEADERS.mkdir(parents=True, exist_ok=True)

    (XCODEPROJ / "project.pbxproj").write_text(PBXPROJ, encoding="utf-8")
    (SOURCES / f"{PROJECT_NAME}.swift").write_text(SWIFT_FILE, encoding="utf-8")
    (HEADERS / f"{PROJECT_NAME}.h").write_text(HEADER_FILE, encoding="utf-8")
    (ROOT / "Info.plist").write_text(INFO_PLIST, encoding="utf-8")

    print(f"Created Cocoa framework project at: {ROOT}")
    print(f"Open with: open '{XCODEPROJ}'")

if __name__ == "__main__":
    main()
