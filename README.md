# PlantUML 使用範例指引

- 系統架構圖
- 類別圖

```
@startuml component
actor client
node app
database db

db -> app
app -> client
@enduml
```

@startuml component
actor client
node app
database db

db -> app
app -> client
@enduml

![系統架構](docs/diagrams/out/test/component.png)

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

![PaymentDetail Class](docs/diagrams/out/test-001/test-001.png)
