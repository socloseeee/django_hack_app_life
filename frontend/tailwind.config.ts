import type { Config } from 'tailwindcss';
// import defaultTheme from 'tailwindcss/defaultTheme'

export default <Partial<Config>>{
  theme: {
    extend: {
      // colors: {
      //   primary: defaultTheme.colors.green
      // },
      colors: {
        'rtk-slate': '#7B939B',
        'rtk-orange': '#FF4F12',
        'rtk-red': '#850337',
        'rtk-dark-blue': '#273A64',
        'rtk-dark-slate': '#313A49',
        'rtk-purple': '#7700FF',
        'rtk-grey': '#F1F3F5',
        'rtk-black': '#101828',
      },
      transitionProperty: {
        flow: 'background-position',
      },
      backgroundSize: {
        flow: '400% auto',
      },
      backgroundImage: {
        'nuxt-gradient':
          'linear-gradient(30deg,#475569,#475569 25%,#0007dc 50%,#5400dc 75%,#dc00bf)',
      },
    },
  },
};
