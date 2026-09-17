# Nano Banana 图片编辑提示词 🍌

<p>
  <a href="README.md"><img src="assets/ui/language-en-inactive.svg" alt="English" width="112" height="32"></a>&nbsp;
  <a href="README_zh.md"><img src="assets/ui/language-zh-CN-active.svg" alt="简体中文 — 当前语言" width="128" height="32"></a>
</p>

让你的照片拥有更多可能。这里收录 Nano Banana 图片编辑提示词，涵盖虚拟试衣、人像合照、产品场景、家居改造与照片修复。每个案例提供独立操作步骤和完整提示词，并逐步补充编辑前后对比，方便你用自己的图片尝试。由 SeeAPI 整理，提供完整中英文版本。

**27 个编辑提示词 · 27 个案例附示例图 · 更新于 2026-09-17**

⭐ Star 收藏这个仓库，为下一次图片编辑寻找灵感。

<a id="featured"></a>

## ✨ 精选玩法

| [虚拟试衣](#p01-complete-look) | [产品换背景](#p02-product-background) | [彩色毛线刺绣](#p28-colorful-yarn-embroidery) | [合照](#p03-shared-portrait) |
| :---: | :---: | :---: | :---: |
| <b>Before → After</b><br><a href="assets/portraits/reference-man.png"><img src="assets/portraits/reference-man.png" width="42" height="42" alt="图 1"></a> <a href="assets/portraits/reference-outfit.png"><img src="assets/portraits/reference-outfit.png" width="42" height="42" alt="图 2"></a> &nbsp;→&nbsp; <a href="assets/portraits/result-virtual-try-on.jpg"><img src="assets/portraits/result-virtual-try-on.jpg" width="90" height="90" alt="虚拟试衣"></a> | <b>Before → After</b><br><a href="assets/products/reference-seeapi-mug.jpg"><img src="assets/products/reference-seeapi-mug.jpg" width="90" height="90" alt="产品原图"></a> &nbsp;→&nbsp; <a href="assets/products/result-mug-ice-background.jpg"><img src="assets/products/result-mug-ice-background.jpg" width="90" height="90" alt="冰雪背景"></a> | <b>Before ↓ After</b><br><a href="assets/colorful-yarn-embroidery/source-example-01.webp"><img src="assets/colorful-yarn-embroidery/source-example-01.webp" width="90" height="180" alt="毛线刺绣 — 原帖对比图 1"></a> | <b>Before → After</b><br><a href="assets/portraits/reference-man.png"><img src="assets/portraits/reference-man.png" width="42" height="42" alt="图 1"></a> <a href="assets/portraits/reference-woman.png"><img src="assets/portraits/reference-woman.png" width="42" height="42" alt="图 2"></a> &nbsp;→&nbsp; <a href="assets/portraits/result-group-photo-updated.jpg"><img src="assets/portraits/result-group-photo-updated.jpg" width="90" height="90" alt="合照"></a> |
| `人物 + 穿搭 → 虚拟试衣` | `产品 + 背景描述 → 新场景` | `原图 → 彩色刺绣` | `两张人像 → 合照` |

## 📑 目录

**仓库指南**

- [✨ 精选玩法](#featured)
- [🧭 模型选择](#how-to-use)
- [📄 许可协议](#license)

**提示词分类**

- [👗 人像与穿搭](#portraits-outfits)
- [🛍️ 产品与商业图片](#products-commercial)
- [🏡 家居与空间](#homes-spaces)
- [🎨 风格转换与趣味创作](#style-transformations)
- [🪄 照片修复与局部调整](#restoration-adjustments)

<a id="how-to-use"></a>

## 🧭 模型选择

| 模型 | 适合 | 注意 |
| --- | --- | --- |
| Nano Banana | 复现初代案例 | 旧款 |
| Nano Banana 2 | 日常编辑、多图合成 | 默认推荐 |
| Nano Banana 2 Lite | 简单编辑、低成本批量处理 | 仅 1K；不擅长多图与连续编辑 |
| Nano Banana Pro | 复杂精修、品牌一致性 | 高要求任务首选 |

<a href="https://nanobanana.seeapi.com/">
  <img src="assets/ui/seeapi-nano-banana-zh-CN.svg" alt="在 SeeAPI 体验 Nano Banana — 立即体验" width="840" height="144">
</a>

<a id="portraits-outfits"></a>

## 👗 1. 人像与穿搭

<a id="p01-complete-look"></a>

### 1.1. 虚拟试衣

#### 🖼️ 预览

| Before | After |
| :---: | :---: |
| <a href="assets/portraits/reference-man.png"><img src="assets/portraits/reference-man.png" width="150" height="150" alt="图 1"></a> &nbsp; <a href="assets/portraits/reference-outfit.png"><img src="assets/portraits/reference-outfit.png" width="150" height="150" alt="图 2"></a><br>人物 + 穿搭 | <a href="assets/portraits/result-virtual-try-on.jpg"><img src="assets/portraits/result-virtual-try-on.jpg" width="320" height="320" alt="虚拟试衣"></a> |

#### 👇 工作流

`人物 + 穿搭 → 虚拟试衣`

#### 📝 完整提示词

```text
根据图 2 及其他参考图中的全部服装与配饰，编辑图 1。让人物穿上完整参考造型，包括参考图提供的上装、下装或连衣裙、外套、鞋子、包袋、首饰、眼镜、腰带和帽饰。转移所有可见穿搭单品，不遗漏小配饰，也不凭空添加单品。保留每件单品的颜色、材质、图案、形状和可辨识设计细节。

保持人物的脸部、身份、发型、肤色、体型与身体比例不变。让衣服自然合身、层次合理，呈现真实的面料垂坠、开合结构、接触阴影及恰当的配饰位置。左右鞋子保持一致。匹配原场景的透视、光照和色温。尽量保留原姿势与背景；如果原图裁掉了脚部，自然扩展画面以展示完整造型。输出一张协调统一、照片级真实的全身时尚照片，不要拼贴、添加文字或重复肢体。
```

<sub>提示词：SeeAPI</sub>

<a id="p04-mini-me"></a>

### 1.2. Mini Me 迷你分身

#### 🖼️ 预览

| Before | After |
| :---: | :---: |
| <a href="assets/portraits/reference-boy.png"><img src="assets/portraits/reference-boy.png" width="320" height="320" alt="图 1"></a><br>人像 | <a href="assets/portraits/result-mini-me.jpg"><img src="assets/portraits/result-mini-me.jpg" width="179" height="320" alt="Mini Me 迷你分身"></a> |

#### 👇 工作流

`人像 → 迷你分身`

#### 📝 完整提示词

```text
在写实主体周围添加多个可爱的 3D 风格 Q 版迷你分身，它们与主体是同一个人，具有相同的面部特征、发型、身体比例和穿搭。
让这些 Q 版小人自然分布在主体周围，以可爱且不喧宾夺主的方式，与她或附近的元素进行俏皮互动。

在画面上叠加鲜活的手绘涂鸦效果：主体周围柔和的白色描边、俏皮的闪光、涂鸦爱心、小花、笑脸图标，以及漂浮的白色手写短语，例如 "shine"、"bright day" 和 "happy"。

将超写实摄影与色彩丰富、柔和的卡通插画无缝融合。
保持主体原本的脸部、体型和身体比例不变。
```

<sub>用户提供提示词 · 原作者与来源待补充</sub>

<a id="p05-pet-photobomb"></a>

### 1.3. 和宠物的搞怪合影

#### 🖼️ 预览

| Before | After |
| :---: | :---: |
| <a href="assets/portraits/reference-woman.png"><img src="assets/portraits/reference-woman.png" width="150" height="150" alt="图 1"></a> &nbsp; <a href="assets/portraits/reference-cat.png"><img src="assets/portraits/reference-cat.png" width="150" height="150" alt="图 2"></a><br>人物 + 宠物 | <a href="assets/portraits/result-pet-selfie.jpg"><img src="assets/portraits/result-pet-selfie.jpg" width="179" height="320" alt="和宠物的搞怪合影"></a> |

#### 👇 工作流

`人物 + 宠物 → 搞怪自拍`

#### 📝 完整提示词

```text
以图 1 作为人物身份参考，图 2 作为宠物身份参考。保留人物可辨识的脸部，以及宠物的物种、毛色花纹和独特特征。

创作一张搞笑的极端 0.5x 广角仰拍自拍，宠物俏皮地抢镜。宠物的鼻子和脸以柔和模糊的细节占据前景大部分空间，带有滑稽的广角畸变。宠物后方的人穿着舒适的奶油色针织毛衣，忍不住大笑，同时保留足够的脸部可见区域以辨认人物。

他们坐在温馨且有美感的咖啡馆里，周围是木质家具、悬挂植物、糕点和柔和金色午后光线。弯曲透视、随性生活片段、抓拍瞬间、高 ISO 手机摄影、自然瑕疵。保留人物身份，不强加其他年龄或性别。输出一张真实可信的照片。
```

<sub>基于用户提供提示词 · 原作者与来源待补充 · SeeAPI 改编：补充人物与宠物参考图约束，调整前景描述并去除年龄、性别限定</sub>

<a id="p06-hairstyle-grid"></a>

### 1.4. 3 × 3 发型九宫格

#### 🖼️ 预览

| Before | After |
| :---: | :---: |
| <a href="assets/portraits/reference-hairstyle.png"><img src="assets/portraits/reference-hairstyle.png" width="213" height="320" alt="图 1"></a><br>人像 | <a href="assets/portraits/result-hairstyle-grid.jpg"><img src="assets/portraits/result-hairstyle-grid.jpg" width="320" height="320" alt="3 × 3 发型九宫格"></a> |

#### 👇 工作流

`人像 → 九种发型`

#### 📝 完整提示词

```text
根据上传的人像，生成一张干净的 3 × 3 九宫格，恰好包含九个大小相同的同一人物头肩肖像。每格都保留完全一致的面部身份、脸型、年龄、肤色、表情、已有面部毛发、服装、相机角度、背景和光照。只改变头发造型，九格保持原有发色一致。

按从左到右、从上到下的顺序呈现九种明显不同的发型：(1) 贴头寸发；(2) 有纹理的精灵短发；(3) 侧分短发配两侧铲短；(4) 齐下巴的一刀切波波头；(5) 带八字刘海的齐肩层次发；(6) 中分长直发；(7) 侧分长款大波浪；(8) 蓬松紧密卷发；(9) 发际线整洁的光滑高丸子头。让每款发型真实适配此人的头型和面部，不改变身份或性别呈现。这些发型适用于任何性别，不要将脸部男性化或女性化。

每格完整展示头发，保持一致取景和窄而均匀的间隔。九种发型必须清晰不同，不重复发型、不缺格、不增加面孔、标签或水印。
```

<sub>提示词：SeeAPI</sub>

<a id="p07-linkedin-headshot"></a>

### 1.5. LinkedIn 职业头像

#### 🖼️ 预览

| Before | After |
| :---: | :---: |
| <a href="assets/portraits/reference-woman.png"><img src="assets/portraits/reference-woman.png" width="320" height="320" alt="图 1"></a><br>人像 | <a href="assets/portraits/result-linkedin.jpg"><img src="assets/portraits/result-linkedin.jpg" width="320" height="320" alt="LinkedIn 职业头像"></a> |

#### 👇 工作流

`人像 → 职业头像`

#### 📝 完整提示词

```text
将上传的人像编辑为精致、亲和的 LinkedIn 职业头像。保留人物准确身份、面部结构、年龄、肤色、发型和自然皮肤纹理，不重塑脸部、不美白肤色，也不改变性别呈现。

采用居中的头肩构图、挺拔但放松的姿势、直视镜头的眼神和轻微自然微笑。让人物穿着整洁低调、符合其原有气质的职业服装。使用柔和虚化的中性灰背景，以及柔和棚拍光线、轻微面部阴影和自然眼神光。仅修饰暂时性的干扰细节，保留独特特征。

输出正方形写实照片，头顶留白适当，脸部周围保留足够空间以适配圆形头像裁切。不要文字、标志、重度美颜或塑料质感皮肤。
```

<sub>提示词：SeeAPI</sub>

<a id="p03-shared-portrait"></a>

### 1.6. 合照

#### 🖼️ 预览

| Before | After |
| :---: | :---: |
| <a href="assets/portraits/reference-man.png"><img src="assets/portraits/reference-man.png" width="150" height="150" alt="图 1"></a> &nbsp; <a href="assets/portraits/reference-woman.png"><img src="assets/portraits/reference-woman.png" width="150" height="150" alt="图 2"></a><br>人物 A + 人物 B | <a href="assets/portraits/result-group-photo-updated.jpg"><img src="assets/portraits/result-group-photo-updated.jpg" width="320" height="320" alt="合照"></a> |

#### 👇 工作流

`两张人像 → 合照`

#### 📝 完整提示词

```text
将图 1 中的人物与图 2 中的人物合成为一张自然合照，让两人在柔和光线的户外场景中并肩站立。分别保留两人的面部特征、年龄、肤色、发型与可辨识身份，不混合脸部，也不要把两人变成同一个人。

采用统一相机视角，以及一致的透视、尺度、光照、色温和景深。让两人神情轻松友好，姿势协调可信，手部解剖正确、间距自然。保留原有穿搭，按需要调整衣褶和阴影。输出一张照片级真实的双人合照，恰好两个人，不要分屏、边框、新增文字或拼贴接缝。
```

<sub>提示词：SeeAPI</sub>

<a id="products-commercial"></a>

## 🛍️ 2. 产品与商业图片

<a id="p02-product-background"></a>

### 2.1. 产品换背景

#### 🖼️ 预览

| Before | After |
| :---: | :---: |
| <a href="assets/products/reference-seeapi-mug.jpg"><img src="assets/products/reference-seeapi-mug.jpg" width="320" height="320" alt="产品原图"></a><br>产品 | <a href="assets/products/result-mug-ice-background.jpg"><img src="assets/products/result-mug-ice-background.jpg" width="320" height="320" alt="冰雪背景"></a> |

#### 👇 工作流

`产品 + 背景描述 → 新场景`

#### 📝 完整提示词

```text
编辑上传的产品照片，将背景替换为 [background_description]。保持产品的准确轮廓、比例、颜色、材质、标志、标签文字和包装细节不变，不重新设计或复制产品。

通过合理的尺度、透视、表面接触关系以及匹配的光照方向、反射和阴影，让产品自然融入新场景。产品应清晰可见、对焦锐利，仅在合适位置使用背景景深。输出一张精致的商业照片，不添加文字、装饰性标志或无关产品。
```

<sub>提示词：SeeAPI</sub>

<a id="p08-white-background-product"></a>

### 2.2. 白底产品图

#### 🖼️ 预览

| Before | After |
| :---: | :---: |
| <a href="assets/products/reference-seeapi-mug.jpg"><img src="assets/products/reference-seeapi-mug.jpg" width="320" height="320" alt="产品原图"></a><br>产品 | <a href="assets/products/result-mug-white-background.jpg"><img src="assets/products/result-mug-white-background.jpg" width="320" height="320" alt="白底产品图"></a> |

#### 👇 工作流

`产品 → 白底产品图`

#### 📝 完整提示词

```text
将上传的产品照片转换为纯白色（#FFFFFF）背景的干净电商棚拍图。只保留目标产品，移除原有环境和无关道具。保留产品的准确形状、比例、颜色、材质、纹理、标志、标签文字及所有可见组件。

让产品居中、四周留白均匀，完整位于画面内。使用柔和均匀的棚拍光线、准确色彩、清晰边缘，并在产品正下方保留轻微自然接触阴影。去除背景偏色和边缘光晕，但不抹除透明部件、精细结构或真实反射。不要重新设计产品、编造不可见结构、添加促销文字或装饰物。
```

<sub>提示词：SeeAPI</sub>

<a id="p09-floating-food-ad"></a>

### 2.3. 悬浮食物广告

#### 🖼️ 预览

原帖示例

<a href="assets/floating-food-ad/source-example-01.webp"><img src="assets/floating-food-ad/source-example-01.webp" width="500" height="500" alt="悬浮食物广告 — 原帖示例"></a>

#### 👇 工作流

`食品 + 食材描述 → 悬浮广告`

#### 📝 完整提示词

```text
以上传食品照片作为 [subject] 的参考，将其可辨识层次拆分为悬浮在白色台面上方、令人有食欲的竖向排列。在堆叠周围加入少量悬空的 [ingredient_bits] 点缀。保留食品特有的食材、颜色、比例和表面纹理。

在排列周围留出充足白色空间。使用大型柔光光源照明，清楚呈现湿润表面、碎屑和切面细节。各层应具有可信的厚度与一致透视，在构图下方保留轻微阴影。输出精致的食品广告图片，不新增文字或无关包装。
```

<sub>创意参考 [@azed_ai](https://x.com/azed_ai/status/2073769875940786430) · [Source: X](https://x.com/azed_ai/status/2073769875940786430) · [原帖提示词](https://x.com/azed_ai/status/2073769888691441721) · SeeAPI 重新编写为参考图编辑提示词，非原文转载；未实测 · 原帖示例，非改写提示词的实测结果。</sub>

<a id="p10-low-angle-product-campaign"></a>

### 2.4. 低机位产品广告

#### 🖼️ 预览

原帖示例

<a href="assets/low-angle-product-campaign/source-example-01.webp"><img src="assets/low-angle-product-campaign/source-example-01.webp" width="500" height="500" alt="低机位产品广告 — 原帖示例"></a>

#### 👇 工作流

`产品 + 人像 → 低机位广告`

#### 📝 完整提示词

```text
围绕图 1 中的 [product name] 制作时尚广告。让人物伸手握住产品，靠近低机位相机，使包装成为画面中最大、最清晰的元素。人物全身站姿位于其后方，背景为白色摄影棚。如果提供图 2，保留该人物身份。

保留产品品牌、清晰标签、几何形状和表面质感。采用自信姿势、鲜明服装和明亮柔光，握持自然、手指正确。通过相机透视制造大小对比，不拉伸包装。人物略虚于产品，不添加广告文案。
```

<sub>创意参考 [@azed_ai](https://x.com/azed_ai/status/2037168464801259602) · [Source: X](https://x.com/azed_ai/status/2037168464801259602) · [原帖提示词](https://x.com/azed_ai/status/2037168488754929910) · SeeAPI 重新编写为参考图编辑提示词，非原文转载；未实测 · 原帖示例，非改写提示词的实测结果。</sub>

<a id="p11-doodle-product-ad"></a>

### 2.5. 手绘涂鸦产品广告

#### 🖼️ 预览

原帖示例

<a href="assets/doodle-product-ad/source-example-01.webp"><img src="assets/doodle-product-ad/source-example-01.webp" width="500" height="500" alt="手绘涂鸦产品广告 — 原帖示例"></a>

#### 👇 工作流

`产品 + 涂鸦创意 → 创意广告`

#### 📝 完整提示词

```text
将上传照片中的产品重新布置为 [product setup]，放在温暖米色灰泥墙旁的简洁台面上。保留包装形状、材质、颜色及品牌信息。用斜向窗光形成延长的阴影与安静的编辑摄影氛围。

用细白色速写线条画出俏皮的 [character]，让它根据构图与真实产品互动，例如倚靠、搬动或从产品后方探头。产品保持摄影质感，角色则明确呈现手绘效果。不要遮挡标签。采用留白充足的正方形构图，道具克制，不添加其他文字。
```

<sub>创意参考 [@azed_ai](https://x.com/azed_ai/status/2053142448533377048) · [Source: X](https://x.com/azed_ai/status/2053142448533377048) · [原帖提示词](https://x.com/azed_ai/status/2053142472222802430) · SeeAPI 重新编写为参考图编辑提示词，非原文转载；未实测 · 原帖示例，非改写提示词的实测结果。</sub>

<a id="p12-packaging-dieline"></a>

### 2.6. 包装展开概念图

#### 🖼️ 预览

原帖示例

<a href="assets/packaging-dieline/source-example-01.webp"><img src="assets/packaging-dieline/source-example-01.webp" width="500" height="281" alt="包装展开概念图 — 原帖示例"></a>

#### 👇 工作流

`包装 → 展开概念图`

#### 📝 完整提示词

```text
根据上传的盒装产品照片，可视化一种可能的包装展开布局。将可见盒面组织为相互连接的平面展开结构，采用正上方视角。把可见图案和文字转移到对应面板，不拉伸变形。使用白色画布，以连续线表示外侧裁切轮廓，断续线表示折痕。

将不可见的折翼和面板视为暂定设计推测，未知图案区域留白。面板连接关系应合理，但不要编造尺寸或宣称制造精度。输出用于讨论包装结构的清晰概念插图，不作为生产裁切文件。
```

<sub>创意参考 [@AmirMushich](https://x.com/AmirMushich/status/2003849723837616489) · [Source: X](https://x.com/AmirMushich/status/2003849723837616489) · [原帖提示词](https://x.com/AmirMushich/status/2003849730355236967) · SeeAPI 重新编写为参考图编辑提示词，非原文转载；未实测 · [作者补充：用于概念探索](https://x.com/AmirMushich/status/2003973666078331060) · 上游灵感: [Salma Aboukar](https://x.com/Salmaaboukarr/status/1994017531699278056) · 原帖示例，非改写提示词的实测结果。</sub>

<a id="homes-spaces"></a>

## 🏡 3. 家居与空间

<a id="p13-interior-design"></a>

### 3.1. 室内设计

#### 🖼️ 预览

| Before | After |
| :---: | :---: |
| <a href="assets/interior-design/reference-room.png"><img src="assets/interior-design/reference-room.png" width="320" height="320" alt="毛坯房间"></a><br>房间 | <a href="assets/interior-design/result-interior.jpg"><img src="assets/interior-design/result-interior.jpg" width="320" height="320" alt="装修后的房间"></a> |

#### 👇 工作流

`房间 + 风格 → 室内改造`

#### 📝 完整提示词

```text
将上传照片中的室内重新设计为 [interior_style] 风格。保留房间实际尺寸、相机视角、层高、墙体、窗户、门和结构特征。为家具、灯具、织物、地毯与装饰制定协调方案，适配现有空间并保留实用动线。

采用真实家具尺寸以及协调的材质和颜色。遵循现有窗户的自然光方向，添加合理灯具并保持阴影一致。不要堵塞门或通道。从原相机角度输出一张写实效果图，呈现可实现的室内改造，不要变成另一个房间。不要平面图、拼贴或新增文字。
```

<sub>提示词：SeeAPI</sub>

<a id="p14-landscape-design"></a>

### 3.2. 庭院景观设计

#### 🖼️ 预览

| Before | After |
| :---: | :---: |
| <a href="assets/landscape-design/reference-yard.png"><img src="assets/landscape-design/reference-yard.png" width="320" height="320" alt="原庭院"></a><br>花园 / 庭院 | <a href="assets/landscape-design/result-landscape.jpg"><img src="assets/landscape-design/result-landscape.jpg" width="320" height="320" alt="改造后的庭院"></a> |

#### 👇 工作流

`庭院 + 风格 + 地区 → 景观设计`

#### 📝 完整提示词

```text
将上传图片中的花园或庭院重新设计为 [landscape_style] 风格。保留现有地块边界、建筑占地、入口、大型结构、地形坡度及相机视角。将种植区、步道、地被、户外座椅和适度景观照明安排成实用且协调的设计。

根据 [climate_or_location] 选择视觉协调的植物组合，体现合理的成株尺寸与种植间距。确保通道可用，不让植物或家具穿过墙体或铺装。匹配原图时段，呈现真实的土壤、石材、植被、透视和阴影。输出同一处场地的一张写实景观效果图，不加标签或平面图叠层。
```

<sub>提示词：SeeAPI</sub>

<a id="p15-furniture-replacement"></a>

### 3.3. 家具替换

#### 🖼️ 预览

**沙发替换**

| Before | After |
| :---: | :---: |
| <a href="assets/interior-design/result-interior.jpg"><img src="assets/interior-design/result-interior.jpg" width="150" height="150" alt="房间"></a> &nbsp; <a href="assets/furniture-replacement/reference-sofa.png"><img src="assets/furniture-replacement/reference-sofa.png" width="150" height="150" alt="沙发参考"></a><br>房间 + 沙发 | <a href="assets/furniture-replacement/result-sofa.jpg"><img src="assets/furniture-replacement/result-sofa.jpg" width="320" height="320" alt="沙发替换效果"></a> |

**挂画替换**

| Before | After |
| :---: | :---: |
| <a href="assets/interior-design/result-interior.jpg"><img src="assets/interior-design/result-interior.jpg" width="150" height="150" alt="房间"></a> &nbsp; <a href="assets/furniture-replacement/reference-artwork.png"><img src="assets/furniture-replacement/reference-artwork.png" width="150" height="150" alt="挂画参考"></a><br>房间 + 挂画 | <a href="assets/furniture-replacement/result-artwork.jpg"><img src="assets/furniture-replacement/result-artwork.jpg" width="320" height="320" alt="挂画替换效果"></a> |

#### 👇 工作流

`房间 + 新家具 / 装饰 → 替换`

#### 📝 完整提示词

```text
编辑图 1，将 [furniture_to_replace] 替换为 [new_furniture_description]。这两个字段可描述家具或装饰品，例如沙发或墙上挂画。如果提供了额外参考图，替换物品应匹配参考物品的设计、材质、颜色和独特细节，不要复制参考图中的周围场景。

保持建筑结构、窗户、门、相机视角以及所有未选中的家具和装饰不变。让替换物品以真实的比例、透视、位置、反射与阴影自然融入房间。替换挂画时，保留参考画作的构图，并使其贴合墙面透视。干净移除选中的旧物品，补全新露出的背景。不要重新设计房间其他部分。保持行走路线畅通，输出一张写实的房间编辑图。
```

<sub>提示词：SeeAPI</sub>

<a id="p16-material-swap"></a>

### 3.4. 自定义材质替换

#### 🖼️ 预览

| Before | After |
| :---: | :---: |
| <a href="assets/material-swap/reference-leather.png"><img src="assets/material-swap/reference-leather.png" width="320" height="320" alt="皮质沙发"></a><br>物体 | <a href="assets/material-swap/result-velvet.jpg"><img src="assets/material-swap/result-velvet.jpg" width="320" height="320" alt="丝绒沙发"></a> |

#### 👇 工作流

`物体 + 材质 → 材质替换`

#### 📝 完整提示词

```text
在上传照片中，只将 [target_object] 的表面材质改为 [material]。保留物体的准确形状、尺寸、轮廓、结构、位置和全部功能细节。保持相机、背景、周围物体及构图不变。

按照 [material] 的特性呈现符合物理规律的纹理尺度、纹理走向、粗糙度、反射率和高光。让纹理自然包裹曲面，并符合边缘、接缝和连接结构。匹配现有光照，只更新受材质变化影响的反射与阴影。不变形、不替换、不改色其他无关物体。输出一张写实编辑图。
```

<sub>提示词：SeeAPI</sub>

<a id="p17-wall-paint"></a>

### 3.5. 自定义墙漆颜色

#### 🖼️ 预览

| Before | After |
| :---: | :---: |
| <a href="assets/wall-paint/reference-room.jpg"><img src="assets/wall-paint/reference-room.jpg" width="320" height="320" alt="原房间"></a><br>房间 | <a href="assets/wall-paint/result-blue-walls.jpg"><img src="assets/wall-paint/result-blue-walls.jpg" width="320" height="320" alt="蓝色墙面"></a> |

#### 👇 工作流

`墙面 + 颜色 → 墙漆改色`

#### 📝 完整提示词

```text
将上传室内照片中的 [wall_area] 重新刷为 [paint_color]。只对选中的涂漆墙面应用新颜色。保持天花板、线脚、门、窗、家具、装饰画、地面及其他区域不变。

保留墙面原本的纹理和建筑细节。呈现所选墙漆在房间现有光照下的自然效果，包括可信的明暗变化，不要使用平面的颜色覆盖层。灯具和物体周围的边界应干净准确。保留原取景与透视，输出同一房间的一张写实图片。
```

<sub>提示词：SeeAPI</sub>

<a id="style-transformations"></a>

## 🎨 4. 风格转换与趣味创作

<a id="p18-polaroid"></a>

### 4.1. 宝丽来照片风格

#### 🖼️ 预览

| Before | After |
| :---: | :---: |
| <a href="assets/portraits/result-group-photo-updated.jpg"><img src="assets/portraits/result-group-photo-updated.jpg" width="320" height="320" alt="原照片"></a><br>原图 | <a href="assets/polaroid/result-polaroid.png"><img src="assets/polaroid/result-polaroid.png" width="258" height="320" alt="宝丽来照片"></a> |

#### 👇 工作流

`原图 → 宝丽来风格`

#### 📝 完整提示词

```text
将上传图片转换为可信的复古宝丽来即时成像照片。保留人物身份、表情、主体排列和主要场景。使用柔和直闪光感、略微低饱和色彩、温暖高光、轻微褪色的阴影、细腻胶片颗粒、轻微镜头柔化，以及自然的即时胶片瑕疵，但不要模糊人脸。

将图片放入干净的米白色即时照片边框中，底部边距稍宽。让主要主体完整位于照片区域内，不裁掉重要特征。效果应克制并保持摄影质感。不要添加手写字、日期、说明文字、其他人物或严重破损。
```

<sub>提示词：SeeAPI</sub>

<a id="p19-lego-style"></a>

### 4.2. 乐高积木世界

#### 🖼️ 预览

| Before | After |
| :---: | :---: |
| <a href="assets/portraits/reference-cat.png"><img src="assets/portraits/reference-cat.png" width="320" height="320" alt="原猫咪照片"></a><br>原图 | <a href="assets/lego-style/result-lego.jpg"><img src="assets/lego-style/result-lego.jpg" width="320" height="320" alt="乐高风格猫咪"></a> |

#### 👇 工作流

`原图 → 乐高世界`

#### 📝 完整提示词

```text
将上传场景重建为细节丰富的乐高风格积木微缩景观。保留原构图、相机角度、主体位置、可辨识的服装颜色及主要背景元素。把人物转换为具有表情的小人仔，保留可辨识发型与配饰；使用结构合理、可相互拼接的塑料积木、板件、光面砖和凸点构建环境与物体。

保持积木尺度统一、连接干净，呈现细微注塑纹理与真实微缩布光。用柔和景深重现原场景氛围和光照方向，同时让主要主体清晰。所有可见元素都应属于同一个积木世界。输出一张完成后的微缩景观照片，不添加说明文字或包装。
```

<sub>提示词：SeeAPI</sub>

<a id="p20-ghibli-anime"></a>

### 4.3. 吉卜力动漫

#### 🖼️ 预览

| Before | After |
| :---: | :---: |
| <a href="assets/portraits/result-pet-selfie.jpg"><img src="assets/portraits/result-pet-selfie.jpg" width="179" height="320" alt="原合影"></a><br>原图 | <a href="assets/ghibli-anime/result-anime.jpg"><img src="assets/ghibli-anime/result-anime.jpg" width="179" height="320" alt="吉卜力动画风格"></a> |

#### 👇 工作流

`原图 → 吉卜力动漫`

#### 📝 完整提示词

```text
将上传图片重新演绎为吉卜力风格启发的手绘动漫场景。保留可辨识的人物身份、表情、姿势、构图和主体之间的关系。使用细腻且富有表现力的线条、柔和水彩般背景、轻柔赛璐璐阴影、温暖自然的色彩与氛围光线。

将真实细节转化为统一的插画世界，环境丰富、观察细致，呈现平静而真挚的日常氛围。让主要面部特征仍可辨认，不把所有人画成同一张脸。保留原场景，不引入现有电影角色或替换场景。输出一幅完整插画，不加说明文字、标志或边框。
```

<sub>提示词：SeeAPI</sub>

<a id="p21-miniature-figurine"></a>

### 4.4. 收藏级迷你手办

#### 🖼️ 预览

| Before | After |
| :---: | :---: |
| <a href="assets/miniature-figurine/reference-toy.png"><img src="assets/miniature-figurine/reference-toy.png" width="320" height="320" alt="角色参考"></a><br>人像 / 角色 | <a href="assets/miniature-figurine/result-figurine.jpg"><img src="assets/miniature-figurine/result-figurine.jpg" width="320" height="320" alt="迷你手办"></a> |

#### 👇 工作流

`角色 → 收藏手办`

#### 📝 完整提示词

```text
以上传图片中的人物或角色为基础，创作一张 1/7 比例收藏级手办的写实产品照片。保留可辨识的脸部、发型、服装、姿势和配饰，将其转化为精细雕刻、上色的树脂手办。呈现可信的微缩比例，以及细致的衣褶、发丝和材质表面处理。

将完整手办放在整洁桌面上的透明圆形亚克力底座上。后方电脑屏幕展示同一手办的灰色 3D 雕刻模型，旁边竖立一个印有同一角色平面插画的收藏包装盒。以手办为清晰焦点，背景柔和虚化。使用自然的桌边光线、真实尺度与轻微树脂反光。包装盒、屏幕和底座上不要品牌标志或可读文字。输出一张照片。
```

<sub>提示词：SeeAPI</sub>

<a id="p22-oil-painting"></a>

### 4.5. 油画风格

#### 🖼️ 预览

| Before | After |
| :---: | :---: |
| <a href="assets/landscape-design/reference-yard.png"><img src="assets/landscape-design/reference-yard.png" width="320" height="320" alt="庭院原图"></a><br>原图 | <a href="assets/oil-painting/result-oil-painting.jpg"><img src="assets/oil-painting/result-oil-painting.jpg" width="320" height="320" alt="油画效果"></a> |

#### 👇 工作流

`原图 → 油画`

#### 📝 完整提示词

```text
将上传图片转换为画布上纹理丰富的油画。保留主要主体的身份、表情、比例、姿势、构图及重要场景细节。用明确可见的笔触、叠加颜料、轻微厚涂高光和协调的绘画色彩来表现形体。

通过合理光影保持空间深度，把细碎摄影噪点简化为富有表现力的笔触。让面孔和关键物体保持可辨认，不扭曲特征，也不要只在照片上叠加均匀的数字纹理。让画作本身铺满画面，不添加画框、签名、标签或画廊场景。
```

<sub>提示词：SeeAPI</sub>

<a id="p28-colorful-yarn-embroidery"></a>

### 4.6. 彩色毛线刺绣

#### 🖼️ 预览

| Before ↓ After | Before ↓ After |
| :---: | :---: |
| <a href="assets/colorful-yarn-embroidery/source-example-01.webp"><img src="assets/colorful-yarn-embroidery/source-example-01.webp" width="200" height="400" alt="毛线刺绣 — 原帖对比图 1"></a> | <a href="assets/colorful-yarn-embroidery/source-example-02.webp"><img src="assets/colorful-yarn-embroidery/source-example-02.webp" width="200" height="400" alt="毛线刺绣 — 原帖对比图 2"></a> |
| <a href="assets/colorful-yarn-embroidery/source-example-03.webp"><img src="assets/colorful-yarn-embroidery/source-example-03.webp" width="200" height="400" alt="毛线刺绣 — 原帖对比图 3"></a> | <a href="assets/colorful-yarn-embroidery/source-example-04.webp"><img src="assets/colorful-yarn-embroidery/source-example-04.webp" width="200" height="400" alt="毛线刺绣 — 原帖对比图 4"></a> |

#### 👇 工作流

`原图 → 彩色刺绣`

#### 📝 完整提示词

```text
根据上传照片制作竖向对比图：上方为原图，下方为彩色毛线刺绣演绎。上下两部分尺寸相同，上方原图保持不变，不添加边框或标签。

将下方场景重构为象牙白织布上的立体手工布贴。使用粗线勾边、毛线线圈、层叠针脚和细小浮雕阴影。保留人物、姿势、服装颜色、标志性物体和主要动作，简化杂乱背景。原本背对镜头的脸仍应背对镜头。所有画面元素都应像缝制而成，而非印刷。以柔和棚拍光线，从正面拍摄这件刺绣作品。

在刺绣场景下方居中绣出三行文字：[TITLE]、[EDITION] 和 [CAPTION]。标题采用粗厚立体字，下方使用较小针脚。用户提供的文字原样保留。未填写的字段自动生成简短英文标题和温暖短句，版次默认使用 PATCH NO. 01。不要显示占位符方括号。仅输出完成的对比图。
```

<sub>创意参考 [@ai_suxiaole](https://x.com/ai_suxiaole/status/2099824477173690831) · [Source: X](https://x.com/ai_suxiaole/status/2099824477173690831) · [原帖提示词](https://x.com/ai_suxiaole/status/2099824480772374956) · SeeAPI 重新编写为参考图编辑提示词，非原文转载；未实测 · 原帖示例，非改写提示词的实测结果。</sub>

<a id="restoration-adjustments"></a>

## 🪄 5. 照片修复与局部调整

<a id="p23-old-photo-restoration"></a>

### 5.1. 老照片修复

#### 🖼️ 预览

原帖示例

| Before | After |
| :---: | :---: |
| <a href="assets/old-photo-restoration/source-example-01.webp"><img src="assets/old-photo-restoration/source-example-01.webp" width="255" height="320" alt="原帖：受损照片"></a><br>老照片 | <a href="assets/old-photo-restoration/source-example-02.webp"><img src="assets/old-photo-restoration/source-example-02.webp" width="255" height="320" alt="原帖：修复效果"></a> |

#### 👇 工作流

`老照片 → 修复照片`

#### 📝 完整提示词

```text
谨慎修复上传的老照片。去除划痕、灰尘、污渍、折痕和扫描瑕疵。依据周围可见信息修复小范围受损区域，改善褪色对比度，恢复自然细节，避免过度锐化或凭空编造五官。

保留原人物身份、年龄、表情、服装、背景、构图和年代特征。黑白照片保持黑白，彩色照片保留原有色调。保留细腻胶片颗粒和自然皮肤纹理，不现代化服装、不添加物体，也不进行美颜。对于已完全丢失的细节，采用克制的重建，不虚构确定细节。输出一张干净、忠实于原图的修复照片，保持原取景。
```

<sub>提示词：SeeAPI · 图片：[@Noor_ul_ain43 · X](https://x.com/Noor_ul_ain43/status/2030189593644126420)；原帖示例，未经下方提示词复现验证</sub>

<a id="p24-add-text"></a>

### 5.2. 在图片中添加文字

#### 🖼️ 预览

| Before | After |
| :---: | :---: |
| <a href="assets/add-text/before.jpg"><img src="assets/add-text/before.jpg" width="320" height="320" alt="原图"></a><br>原图 | <a href="assets/add-text/after.png"><img src="assets/add-text/after.png" width="258" height="320" alt="添加文字"></a> |

#### 👇 工作流

`原图 + 文字 + 位置 → 添加文字`

#### 📝 完整提示词

```text
在上传图片的 [text_location] 位置，以 [text_style] 样式添加原样文字 "[text_content]"。准确复现所提供的措辞、大小写、标点和换行，不翻译、不改写、不增加或遗漏字符。

让文字在预期尺寸下清晰易读、视觉均衡。若文字位于实体表面，应匹配该表面的透视、曲率、纹理、光照和遮挡；若作为平面叠加文字，使用干净排版与合适对比度。保留图片其他部分，包括人脸和已有的无关文字。除非指定位置要求，否则不要遮挡重要主体。输出一张编辑图片，不添加额外说明文字。
```

<sub>提示词：SeeAPI</sub>

<a id="p25-remove-object"></a>

### 5.3. 移除指定物体

#### 🖼️ 预览

| Before | After |
| :---: | :---: |
| <a href="assets/remove-object/before.png"><img src="assets/remove-object/before.png" width="320" height="320" alt="原图"></a><br>原图 | <a href="assets/remove-object/after.png"><img src="assets/remove-object/after.png" width="320" height="320" alt="移除人物"></a> |

#### 👇 工作流

`原图 + 指定物体 → 移除物体`

#### 📝 完整提示词

```text
从上传图片中移除 [object_to_remove]，同时仅移除属于该物体的投影与反射。根据周围场景的纹理、几何结构、透视、光照和景深，无缝补全露出的背景。

保留其他所有人物、物体、边缘和建筑特征。不用新物体替代被移除物体，不移动附近主体，不裁切图片，也不改变整体颜色。避免涂抹、重复纹理、模糊补丁及可见编辑边界。输出一张自然图片，保持原尺寸和取景。
```

<sub>提示词：SeeAPI</sub>

<a id="p26-relight-image"></a>

### 5.4. 图片重新布光

#### 🖼️ 预览

| Before | After |
| :---: | :---: |
| <a href="assets/relight-image/before.png"><img src="assets/relight-image/before.png" width="320" height="320" alt="原图"></a><br>原图 | <a href="assets/relight-image/after.jpg"><img src="assets/relight-image/after.jpg" width="320" height="320" alt="金色夕阳光线"></a> |

#### 👇 工作流

`原图 + 光线描述 → 重新布光`

#### 📝 完整提示词

```text
使用 [lighting_description] 为上传图片重新布光。保持全部主体、身份、姿势、物体形状、材质、相机透视和构图不变。修改照明，不重新设计场景。

应用统一的光照方向、光源尺寸、色温、强度及衰减。在整个场景中一致地更新高光、阴影、眼神光、反射和接触阴影，并在合适位置加入轻微反弹光。保留自然肤色与材质细节，避免高光过曝、暗部死黑、虚假光晕或平面颜色滤镜。输出一张符合指定光照的写实图片，除非明确要求，否则不新增可见灯具。
```

<sub>提示词：SeeAPI</sub>

<a id="license"></a>

## 📄 许可协议

SeeAPI 原创提示词与文档采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh-hans) 许可，欢迎复制、转载与改编，包括商业用途。请署名 **SeeAPI**，附上[本仓库](https://github.com/SeeAPI/nano-banana-prompts-for-image-editing)及许可证链接；如有修改，请注明。

引用的第三方提示词与图片仍遵循原作者的许可，标注来源不等于获得转载授权。详见 [LICENSE.md](LICENSE.md)。
