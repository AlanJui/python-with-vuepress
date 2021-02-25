---
sidebar: auto
---

# PlantUML 使用指引

## PlantUML 應用範例

### 系統架構圖（Componment Diagram）

![系統架構圖](@uml/my-004.png)

```
@startuml component
actor client
node app
database db

db -> app
app -> client
@enduml
```

### 循序圖（Sequence Diagram）

![循序圖](@uml/my-001.png)

### 流程圖

![流程圖](@uml/my-003.png)

### 類別圖（Class Diagram）

```plantuml
@startuml class
class PaymentDetail {
    PMId: autonumber
    CardOwnerName: string
    CardNumber: string
    ExpirationDate: string
    CVV: string
}
@enduml
```

![類別圖](@uml/my-002.png)
