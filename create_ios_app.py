from pathlib import Path

PROJECT_NAME = "MyiOSApp"
ORGANIZATION_IDENTIFIER = "com.example"
BUNDLE_ID = f"{ORGANIZATION_IDENTIFIER}.{PROJECT_NAME}"

DESKTOP = Path.home() / "Desktop"
ROOT = DESKTOP / PROJECT_NAME
XCODEPROJ = ROOT / f"{PROJECT_NAME}.xcodeproj"
ASSETS = ROOT / "Assets.xcassets"
APPICON = ASSETS / "AppIcon.appiconset"

PBXPROJ = f'''// !$*UTF8*$!
{{
	archiveVersion = 1;
	classes = {{
	}};
	objectVersion = 56;
	objects = {{

/* Begin PBXBuildFile section */
		A00000000000000000000011 /* {PROJECT_NAME}App.swift in Sources */ = {{isa = PBXBuildFile; fileRef = A00000000000000000000001 /* {PROJECT_NAME}App.swift */; }};
		A00000000000000000000012 /* ContentView.swift in Sources */ = {{isa = PBXBuildFile; fileRef = A00000000000000000000002 /* ContentView.swift */; }};
		A00000000000000000000013 /* Assets.xcassets in Resources */ = {{isa = PBXBuildFile; fileRef = A00000000000000000000003 /* Assets.xcassets */; }};
		A00000000000000000000014 /* Info.plist in Resources */ = {{isa = PBXBuildFile; fileRef = A00000000000000000000004 /* Info.plist */; }};
		A00000000000000000000015 /* UIKit.framework in Frameworks */ = {{isa = PBXBuildFile; fileRef = A00000000000000000000021 /* UIKit.framework */; }};
		A00000000000000000000016 /* SwiftUI.framework in Frameworks */ = {{isa = PBXBuildFile; fileRef = A00000000000000000000022 /* SwiftUI.framework */; }};
/* End PBXBuildFile section */

/* Begin PBXFileReference section */
		A00000000000000000000001 /* {PROJECT_NAME}App.swift */ = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = {PROJECT_NAME}App.swift; sourceTree = "<group>"; }};
		A00000000000000000000002 /* ContentView.swift */ = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ContentView.swift; sourceTree = "<group>"; }};
		A00000000000000000000003 /* Assets.xcassets */ = {{isa = PBXFileReference; lastKnownFileType = folder.assetcatalog; path = Assets.xcassets; sourceTree = "<group>"; }};
		A00000000000000000000004 /* Info.plist */ = {{isa = PBXFileReference; lastKnownFileType = text.plist.xml; path = Info.plist; sourceTree = "<group>"; }};
		A00000000000000000000021 /* UIKit.framework */ = {{isa = PBXFileReference; lastKnownFileType = wrapper.framework; name = UIKit.framework; path = System/Library/Frameworks/UIKit.framework; sourceTree = SDKROOT; }};
		A00000000000000000000022 /* SwiftUI.framework */ = {{isa = PBXFileReference; lastKnownFileType = wrapper.framework; name = SwiftUI.framework; path = System/Library/Frameworks/SwiftUI.framework; sourceTree = SDKROOT; }};
		A00000000000000000000031 /* {PROJECT_NAME}.app */ = {{isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = {PROJECT_NAME}.app; sourceTree = BUILT_PRODUCTS_DIR; }};
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
		A00000000000000000000041 /* Frameworks */ = {{
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
				A00000000000000000000015 /* UIKit.framework in Frameworks */,
				A00000000000000000000016 /* SwiftUI.framework in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
		A00000000000000000000051 = {{
			isa = PBXGroup;
			children = (
				A00000000000000000000052 /* Sources */,
				A00000000000000000000053 /* Resources */,
				A00000000000000000000054 /* Frameworks */,
				A00000000000000000000055 /* Products */,
			);
			sourceTree = "<group>";
		}};
		A00000000000000000000052 /* Sources */ = {{
			isa = PBXGroup;
			children = (
				A00000000000000000000001 /* {PROJECT_NAME}App.swift */,
				A00000000000000000000002 /* ContentView.swift */,
			);
			sourceTree = "<group>";
		}};
		A00000000000000000000053 /* Resources */ = {{
			isa = PBXGroup;
			children = (
				A00000000000000000000003 /* Assets.xcassets */,
				A00000000000000000000004 /* Info.plist */,
			);
			sourceTree = "<group>";
		}};
		A00000000000000000000054 /* Frameworks */ = {{
			isa = PBXGroup;
			children = (
				A00000000000000000000021 /* UIKit.framework */,
				A00000000000000000000022 /* SwiftUI.framework */,
			);
			name = Frameworks;
			sourceTree = "<group>";
		}};
		A00000000000000000000055 /* Products */ = {{
			isa = PBXGroup;
			children = (
				A00000000000000000000031 /* {PROJECT_NAME}.app */,
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
				A00000000000000000000092 /* Resources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = {PROJECT_NAME};
			productName = {PROJECT_NAME};
			productReference = A00000000000000000000031 /* {PROJECT_NAME}.app */;
			productType = "com.apple.product-type.application";
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
			productRefGroup = A00000000000000000000055 /* Products */;
			projectDirPath = "";
			projectRoot = "";
			targets = (
				A00000000000000000000071 /* {PROJECT_NAME} */,
			);
		}};
/* End PBXProject section */

/* Begin PBXResourcesBuildPhase section */
		A00000000000000000000092 /* Resources */ = {{
			isa = PBXResourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				A00000000000000000000013 /* Assets.xcassets in Resources */,
				A00000000000000000000014 /* Info.plist in Resources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXResourcesBuildPhase section */

/* Begin PBXSourcesBuildPhase section */
		A00000000000000000000091 /* Sources */ = {{
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				A00000000000000000000011 /* {PROJECT_NAME}App.swift in Sources */,
				A00000000000000000000012 /* ContentView.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
		A00000000000000000000101 /* Debug */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				CODE_SIGN_STYLE = Automatic;
				CURRENT_PROJECT_VERSION = 1;
				GENERATE_INFOPLIST_FILE = NO;
				INFOPLIST_FILE = Info.plist;
				IPHONEOS_DEPLOYMENT_TARGET = 17.0;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = {BUNDLE_ID};
				PRODUCT_NAME = "$(TARGET_NAME)";
				SDKROOT = iphoneos;
				SUPPORTED_PLATFORMS = "iphoneos iphonesimulator";
				SWIFT_VERSION = 5.0;
				TARGETED_DEVICE_FAMILY = 1;
			}};
			name = Debug;
		}};
		A00000000000000000000102 /* Release */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				CODE_SIGN_STYLE = Automatic;
				CURRENT_PROJECT_VERSION = 1;
				GENERATE_INFOPLIST_FILE = NO;
				INFOPLIST_FILE = Info.plist;
				IPHONEOS_DEPLOYMENT_TARGET = 17.0;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = {BUNDLE_ID};
				PRODUCT_NAME = "$(TARGET_NAME)";
				SDKROOT = iphoneos;
				SUPPORTED_PLATFORMS = "iphoneos iphonesimulator";
				SWIFT_VERSION = 5.0;
				TARGETED_DEVICE_FAMILY = 1;
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

APP_SWIFT = f'''import SwiftUI

@main
struct {PROJECT_NAME}App: App {{
    var body: some Scene {{
        WindowGroup {{
            ContentView()
        }}
    }}
}}
'''

CONTENT_SWIFT = '''import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack(spacing: 16) {
            Text("Hello, iPhone")
                .font(.largeTitle)

            Text("New iOS app created from Python.")
                .foregroundStyle(.secondary)
        }
        .padding()
    }
}

#Preview {
    ContentView()
}
'''

INFO_PLIST = '''<?xml version="1.0" encoding="UTF-8"?>
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
	<string>APPL</string>
	<key>CFBundleShortVersionString</key>
	<string>$(MARKETING_VERSION)</string>
	<key>CFBundleVersion</key>
	<string>$(CURRENT_PROJECT_VERSION)</string>
	<key>UIApplicationSceneManifest</key>
	<dict>
		<key>UIApplicationSupportsMultipleScenes</key>
		<false/>
	</dict>
	<key>UILaunchScreen</key>
	<dict/>
</dict>
</plist>
'''

CONTENTS_JSON = '''{
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
'''

APPICON_JSON = '''{
  "images" : [

  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
'''

def main():
    XCODEPROJ.mkdir(parents=True, exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)
    APPICON.mkdir(parents=True, exist_ok=True)

    (XCODEPROJ / "project.pbxproj").write_text(PBXPROJ, encoding="utf-8")
    (ROOT / f"{PROJECT_NAME}App.swift").write_text(APP_SWIFT, encoding="utf-8")
    (ROOT / "ContentView.swift").write_text(CONTENT_SWIFT, encoding="utf-8")
    (ROOT / "Info.plist").write_text(INFO_PLIST, encoding="utf-8")
    (ASSETS / "Contents.json").write_text(CONTENTS_JSON, encoding="utf-8")
    (APPICON / "Contents.json").write_text(APPICON_JSON, encoding="utf-8")

    print(f"Created iOS app project at: {ROOT}")
    print(f"Open with: open '{XCODEPROJ}'")

if __name__ == "__main__":
    main()
