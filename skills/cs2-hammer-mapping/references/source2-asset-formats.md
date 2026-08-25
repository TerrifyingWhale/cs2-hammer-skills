# Source 2 资产格式（通用规则）

本参考保留通用资产规则与检查清单。材质、模型、粒子、滤镜、声音、脚本各有独立技能：

- 材质/纹理：CS2 材质创作技能（cs2-material-creation），处理 `.vmat`、`.vtex`。
- 模型：CS2 模型创作技能（cs2-model-creation），处理 `.vmdl`。
- 粒子：CS2 粒子创作技能（cs2-particle-creation），处理 `.vpcf`。
- 滤镜：CS2 滤镜创作技能（cs2-postprocess-creation），处理 `.vpost`。
- 声音：CS2 声音创作技能（cs2-sound-creation），处理 `.vsndevts` / `sounds/`。
- 脚本：CS2 脚本创作技能（cs2-script-creation），处理 `cs_script` / `.js`。

## 核心规则

CS2 和 Hammer 不会直接消费原始美术文件。每个资产都需要一个 Source 2 "配方"文件，由 Hammer 自动编译成引擎资源（`_c` 后缀：`.vmat_c`、`.vtex_c`、`.vmdl_c`、`.vpcf_c`、`.vpost_c`、`.vsnd_c`）。

- 源（未编译）资产位于 `content/csgo_addons/<addon>/...`。
- 引擎实际加载的编译资源位于 `game/csgo_addons/<addon>/...`。
- 编写任何新资产前，先按对应技能的 reference 规范写；addon 现有同类型文件仅作参考。kv3 文件头带有版本 GUID，必须与已安装的 SDK 匹配；凭记忆手写文件头是最常见的失败原因。

## 自动编译

- 在 Hammer 中打开/保存 addon 时，资源会自动编译，无需手动调用编译器。
- 若资产没有生效，检查配方文件内容或源路径是否有误。

## 生成资产时的检查清单

1. 确定资产类型，按对应技能的 reference 规范写（kv3 头版本 GUID 照抄模板）；addon 现有同类型文件仅作参考。
2. 把配方文件写入 addon 的 `content/` 目录树，保证相对路径正确。
3. 在 Hammer 中打开/保存，让资源自动编译；如有报错按提示检查。
4. 交互式创建资产时优先使用 SDK 工具（ModelDoc、Material Editor、Particle Editor）；只有格式简单且完全理解时才手写文本配方。
