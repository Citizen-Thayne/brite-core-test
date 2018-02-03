export class RiskType {
  constructor ({
    name,
    fields,
    id
  }) {
    this.name = name
    this.fields = fields.map(f => new RiskTypeField(f))
    this.id = id
  }
}

export class RiskTypeField {
  DATA_TYPES = {
    NUMBER: 'n',
    TEXT: 't',
    ENUM: 'e',
    DATA: 'd'
  }
  constructor ({
    name,
    dataType
  }) {
    this.name = name
    this.dataType = Object.entries.find([key, value] => value === dataType).  
  }
}
