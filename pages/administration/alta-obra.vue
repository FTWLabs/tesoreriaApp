<template>
  <n-layout
  :content-style="{
    'display': 'flex',
    'flex-direction': 'column',
    'flex-wrap': 'wrap',
    'align-items': 'center',
  }"
  class="alta-obra">
    <n-h1>
      <n-text>
        Alta de obra
      </n-text>
    </n-h1>
    <n-form
    class="form-alta-obra"
    ref="formRef"
    :model="formValue"
    :rules="rules"
    >
      <n-h3
      class="categories-form">
        <n-text>
          Datos de identificación de la obra
        </n-text>
      </n-h3>
      <n-form-item label="Nombre de obra" path="build.name">
        <n-input v-model:value="formValue.build.name" placeholder="Introduzca el nombre de la obra" />
      </n-form-item>
      <n-form-item label="Número de obra" path="build.number">
        <n-input v-model:value="formValue.build.number" placeholder="Introduzca el numero de obra" />
      </n-form-item>
      <n-form-item label="Fecha de inicio" path="build.startDate">
        <n-date-picker v-model:value="formValue.build.startDate" placeholder="Seleccione una fecha"  type="date" />
      </n-form-item>
      <n-form-item label="Fecha de finalización" path="build.finishDate">
        <n-date-picker v-model:value="formValue.build.finishDate" placeholder="Seleccione una fecha"  type="date" />
      </n-form-item>
      <n-form-item label="Director de la obra" path="build.director">
        <n-input v-model:value="formValue.build.director" placeholder="Introduzca el nombre del director" />
      </n-form-item>
      <n-h3
      class="categories-form">
        <n-text>
          Datos contractuales de la obra
        </n-text>
      </n-h3>
      <n-form-item label="Numero de contrato" path="contract.number">
        <n-input v-model:value="formValue.contract.number" placeholder="Introduzca el nombre de contrato" />
      </n-form-item>
      <n-form-item label="Cliente" path="contract.nameCustomer">
        <n-input v-model:value="formValue.contract.nameCustomer" placeholder="Introduzca el nombre del cliente" />
      </n-form-item>
      <n-form-item label="Fecha de contrato" path="contract.date">
        <n-date-picker v-model:value="formValue.contract.date"  placeholder="Seleccione una fecha"  type="date" />
      </n-form-item>
      <n-form-item label="Plazo contractual" path="contract.lapse">
        <n-input v-model:value="formValue.contract.lapse" placeholder="Introduzca el plazo" />
      </n-form-item>
      <n-h3
      class="categories-form">
        <n-text>
          Datos adjudicatarios de la obra
        </n-text>
      </n-h3>
      <n-form-item label="Consorcio adjudicatario" path="adjudge.consortium">
        <n-input v-model:value="formValue.adjudge.consortium" placeholder="Introduzca el consorcio" />
      </n-form-item>
      <n-form-item label="Empresa del grupo adjudicatario" path="adjudge.group">
        <n-input v-model:value="formValue.adjudge.group" placeholder="Introduzca el grupo adjudicatario" />
      </n-form-item>
      <n-form-item label="Porcentaje de participación" path="adjudge.percentage">
        <n-input v-model:value="formValue.adjudge.percentage" placeholder="Introduzca el porcentaje de participación" />
      </n-form-item>
      <n-form-item label="Presupuesto adjudicatario" path="adjudge.budget">
        <n-input v-model:value="formValue.adjudge.budget" placeholder="Introduzca el presupuesto" />
      </n-form-item>
      <n-form-item class="save-button-form">
        <n-button type="primary" round @click="handleValidateButtonClick">
          Guardar
        </n-button>
      </n-form-item>
    </n-form>
    <!--
    This is a preview of the changes in the form
    <pre>{{ JSON.stringify(formValue, null, 2) }}
    </pre>
    -->
  </n-layout>
</template>

<script setup lang="ts">
import {
  NDatePicker,
  NH1,
  NText,
  NH3,
  NLayout,
  NForm,
  NFormItem,
  NInput,
  NButton,
  useMessage,
  FormInst,
  FormRules
} from 'naive-ui'

const formRef = ref<FormInst | null>(null)

const formValue = ref({
  build: {
    name: '',
    number: '',
    startDate: null,
    finishDate: null,
    director: '',
  },
  contract: {
    number: '',
    nameCustomer: '',
    date: null,
    lapse: '',
  },
  adjudge: {
    consortium: '',
    group: '',
    percentage: '',
    budget: '',
  }
})

const rules: FormRules = {
  build: {
    name: {
      required: true,
      trigger: ['blur', 'change'],
      message: 'Por favor introduzca el dato'
    },
    number: {
      required: true,
      trigger: ['blur', 'change'],
      message: 'Por favor introduzca el dato'
    },
    startDate: {
      type: 'number',
      required: true,
      trigger: ['blur', 'change'],
      message: 'Por favor introduzca el dato'
    },
    finishDate: {
      type: 'number',
      required: true,
      trigger: ['blur', 'change'],
      message: 'Por favor introduzca el dato'
    },
    director: {
      required: true,
      trigger: ['blur', 'change'],
      message: 'Por favor introduzca el dato'
    },
  },
  contract: {
    number: {
      required: true,
      trigger: ['blur', 'change'],
      message: 'Por favor introduzca el dato'
    },
    nameCustomer: {
      required: true,
      trigger: ['blur', 'change'],
      message: 'Por favor introduzca el dato'
    },
    date: {
      type: 'number',
      required: true,
      trigger: ['blur', 'change'],
      message: 'Por favor introduzca el dato'
    },
    lapse: {
      required: true,
      trigger: ['blur', 'change'],
      message: 'Por favor introduzca el dato'
    },
  },
  adjudge: {
    consortium: {
      required: true,
      trigger: ['blur', 'change'],
      message: 'Por favor introduzca el dato'
    },
    group: {
      required: true,
      trigger: ['blur', 'change'],
      message: 'Por favor introduzca el dato'
    },
    percentage: {
      required: true,
      trigger: ['blur', 'change'],
      message: 'Por favor introduzca el dato'
    },
    budget: {
      required: true,
      trigger: ['blur', 'change'],
      message: 'Por favor introduzca el dato'
    },
  }
}

function handleValidateButtonClick(e: MouseEvent) {
  e.preventDefault()
  formRef.value?.validate((errors) => {
    if(!errors) {
      //TODO post in server
      console.log(formValue)
    } else {
      console.log('Holas')
    }
  })
}
</script>

<style>
.n-layout.alta-obra {
  margin: 0 0 0 4em;
  padding: 3em 15%;
}

.n-form.form-alta-obra {
  display: flex;
  width: 100%;
  justify-content: space-between;
  flex-wrap: wrap;
}

.n-form.form-alta-obra > .n-form-item {
  width: 45%;
}

.n-h3.categories-form {
  width: 100%;
}

.n-form.form-alta-obra > .n-form-item.save-button-form {
  display: flex;
  width: 100%;
  justify-content: flex-end;
  position: relative;
  padding-bottom: 1em;
}

@media (max-width: 700px) {
  .n-layout.alta-obra {
    margin: 0 0 0 4em;
    padding: 2em 3em;
  }
  .n-form.form-alta-obra >.n-form-item {
    width: 85%;
  }
}

@media (min-width: 700px) and (max-width: 900px) {
  .n-layout.alta-obra {
    margin: 0 0 0 4em;
    padding: 2em 10%;
  }
  .n-form.form-alta-obra >.n-form-item {
    width: 45%;
  }
}
</style>