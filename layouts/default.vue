<template>
  <div>
    <n-layout
    :style="{
      transform: isCollapsed
      ? 'translateX(calc(-80%))'
      : 'translateX(0)',
      borderRadius: '0 5px 5px 0',
      borderRight: 'solid 1px #777',
      boxShadow: '0 0 5px 1px #555'
    }"
    class="sidebar">
      <n-layout-content>
      <div class="content-sidebar">
        <div
        class="header-sidebar">
          <n-h3 :theme-overrides="h3ThemeOverrides">
            <n-text>
              Control de tesorería
            </n-text>
          </n-h3>
          <n-icon
          size="1.5em">
            <n-button
            strong
            secondary
            circle
            @click="setIsCollapsed()">
              <svg
              :style="{
                transform: isCollapsed
                ? 'rotate(0deg)'
                : 'rotate(180deg)',
                transition: '.5s ease'
              }"
              xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 16 16"><g fill="none"><path d="M7.7 4.26a.75.75 0 1 1 1.1-1.02l4 4.25a.75.75 0 0 1 0 1.02l-4 4.25a.75.75 0 1 1-1.1-1.02L11.226 8L7.7 4.26zm-4 0a.75.75 0 1 1 1.1-1.02l4 4.25a.75.75 0 0 1 0 1.02l-4 4.25a.75.75 0 1 1-1.1-1.02L7.227 8L3.7 4.26z" fill="currentColor"></path></g></svg>
            </n-button>
          </n-icon>
        </div>
        <div
        class="home-link">
          <NuxtLink
          to="/"
          :style="{
            display:'flex',
            alignItems: 'center'
          }"
          @click="setIsCollapsed()"
          > 
            <n-icon
            size="1.5em"
            >
              <component
              :is="Home" />
            </n-icon>
            <n-h4
            :theme-overrides="h4ThemeOverrides">
              <n-text>
                Menu
              </n-text>
            </n-h4>
          </NuxtLink>
        </div>
        <div 
        :style="{
          display: isCollapsed
          ? 'none'
          : 'block'
        }"
        class="collapse-main-menu">
          <n-collapse default-expanded-names="1" accordion
          :theme-overrides="collapseThemeOverrides"
          >
          <!--
            <template #header-extra>
              <NuxtLink to="/">
                Holas
              </NuxtLink>
            </template>
            <template #arrow>
              <n-icon>
                <cash-icon />
              </n-icon>
            </template>
          -->
            <n-collapse-item
            v-for="collapseItem in collapseItems"
            class="collapse-title"
            :title="collapseItem.title" :name="collapseItem.title"
            >
              <div
              class="optionsPerTitle"
              v-for="subTitle in collapseItem.subTitle"
              >
                <div
                :style="{
                  display:'flex',
                  marginBottom: '3px'
                }"
                >
                  <n-icon
                  size="1.5em">
                    <component
                    :is="subTitle.icon"
                    />
                  </n-icon>
                  <div
                  :style="{
                    marginLeft: '5px'
                  }"
                  >{{ subTitle.value }}</div>
                </div>
                <ul class="in-sidebar">
                  <li
                  v-for="option in subTitle.item"
                  >
                    <NuxtLink
                    :to="prefixAdmin+option.route"
                    v-if="option.route.length!=0"
                    @click="setIsCollapsed()">
                      {{ option.value }}
                    </NuxtLink>
                  </li>
                </ul>
              </div>
            </n-collapse-item>
          </n-collapse>
        </div>
      </div>
      </n-layout-content>
    </n-layout>
    <slot />
  </div>
</template>
  
<script lang="ts" setup>
import {
  NLayout,
  LayoutProps,
  NLayoutContent,
  NCollapse,
  CollapseProps,
  NCollapseItem,
  NH3,
  H3Props,
  NH4,
  H4Props,
  NText,
  NIcon,
  IconProps,
  NButton,
} from 'naive-ui'

type CollapseThemeOverrides = NonNullable<CollapseProps['themeOverrides']>
type H3ThemeOverrides = NonNullable<H3Props['themeOverrides']>
type H4ThemeOverrides = NonNullable<H4Props['themeOverrides']>
type IconThemeOverrides = NonNullable<IconProps['themeOverrides']>

const iconThemeOverrides: IconThemeOverrides = {

}  
const h3ThemeOverrides: H3ThemeOverrides = {
  headerMargin3: '10px 0 0 37px',
}
const h4ThemeOverrides: H4ThemeOverrides = {
  headerMargin4: '0 0 0 10px',
}
const collapseThemeOverrides: CollapseThemeOverrides = {
  titleFontSize: '16px',
  fontSize: '16px',
  titlePadding: '5px 15px',
  itemMargin: '0',
  dividerColor: 'none',
}

const { isCollapsed, setIsCollapsed} = useIsCollapsed()
const prefixAdmin = '/administration/'
const UserCog = resolveComponent('UserCog')
const BiBuildingFillGear = resolveComponent('BiBuildingFillGear')
const Home = resolveComponent('Home')
resolveComponent('BiBuildingFillGear')
//const MaterialSymbolsHomeRounded = resolveComponent('MaterialSymbolsHomeRounded')

const collapseItems = [
  {
    title: 'Administrador',
    subTitle: [
      {
        value: 'Usuario',
        icon: UserCog,
        item: [
          {
            value: 'Alta de usuarios',
            route: ''
          },
          {
            value: 'Edición de usuarios',
            route: ''
          },
          {
            value: 'Lista de usuarios',
            route: ''
          }
        ]
      },
      {
        value: 'Obra',
        icon: BiBuildingFillGear,
        item: [
          {
            value: 'Alta de obra',
            route: 'alta-obra'
          },
          {
            value: 'Presupuesto de obra',
            route: ''
          },
          {
            value: 'Costes indirectos',
            route: ''
          }
        ]
      },
    ]
  },
  {
    title: 'Planificación de obra',
    subTitle: [
      {
        value: 'Usuario',
        icon: UserCog,
        item: [
          {
            value: 'Alta de usuarios',
            route: ''
          },
          {
            value: 'Edición de usuarios',
            route: ''
          },
          {
            value: 'Lista de usuarios',
            route: ''
          }
        ]
      },
    ]
  },
  {
    title: 'Administración de obra',
    subTitle: [
      {
        value: 'Usuario',
        icon: UserCog,
        item: [
          {
            value: 'Alta de usuarios',
            route: ''
          },
          {
            value: 'Edición de usuarios',
            route: ''
          },
          {
            value: 'Lista de usuarios',
            route: ''
          }
        ]
      },
    ]
  },
  {
    title: 'Informes',
    subTitle: [
      {
        value: 'Usuario',
        icon: UserCog,
        item: [
          {
            value: 'Alta de usuarios',
            route: ''
          },
          {
            value: 'Edición de usuarios',
            route: ''
          },
          {
            value: 'Lista de usuarios',
            route: ''
          }
        ]
      },
    ]
  },
]
</script>
  
<style>
div.collapse-main-menu {
  padding: 10px 0;
  transition: .5s ease;
}

.n-layout.sidebar {
  padding: 20px 0;
  width: 350px;
  height: 100%;
  position: fixed;
  transition: 200ms ease-out;
  z-index: 100;
  overflow-y: auto;
}

div.content-sidebar {
  height: 100%;
}
div.optionsPerTitle {
  padding: 0 0 16px 40px;
}
div.header-sidebar{
  display: flex;
  padding: 15px 0;
  justify-content: space-between;
  margin-right: 2.3em;
}
div.home-link{
  margin: 0 0 0 37px;
}
ul.in-sidebar{
  padding: 6px 1em;
}

@media (max-width: 480px) {
  .n-layout.sidebar {
    width: 90%;
  }
}

.n-layout.sidebar::-webkit-scrollbar {
    display: block;
    width: 8px;
}
.n-layout.sidebar::-webkit-scrollbar-track {
    background: #f7f7f7;
    box-shadow: inset 0 0 4px #a3a3a3;
    border-radius: 5px;
    margin-bottom: .2em;
}
    
.n-layout.sidebar::-webkit-scrollbar-thumb {
    background-color: #919191;
    border-radius: 5px;
}

.n-layout.sidebar::-webkit-scrollbar-track-piece:end {
    background: transparent;
}

.n-layout.sidebar::-webkit-scrollbar-track-piece:start {
    background: transparent;
}
</style>