import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

import arJSON from './locales/ar.json';
import bsJSON from './locales/bs.json';
import deJSON from './locales/de.json';
import enJSON from './locales/en.json';
import frJSON from './locales/fr.json';
import esJSON from './locales/es.json';
import hrJSON from './locales/hr.json';
import itJSON from './locales/it.json';
import ptJSON from './locales/pt.json';
import sqJSON from './locales/sq.json';
import srCyrlJSON from './locales/sr-Cyrl.json';
import srLatnJSON from './locales/sr-Latn.json';
import trJSON from './locales/tr.json';

const resources = {
  ar: { translation: arJSON },
  bs: { translation: bsJSON },
  de: { translation: deJSON },
  en: { translation: enJSON },
  es: { translation: esJSON },
  fr: { translation: frJSON },
  hr: { translation: hrJSON },
  it: { translation: itJSON },
  pt: { translation: ptJSON },
  sq: { translation: sqJSON },
  'sr-Cyrl': { translation: srCyrlJSON },
  'sr-Latn': { translation: srLatnJSON },
  tr: { translation: trJSON },
};

i18n
  .use(initReactI18next)
  .init({
    resources,
    lng: localStorage.getItem('language') ?? 'fr',
    fallbackLng: 'fr',
    supportedLngs: Object.keys(resources),
    interpolation: {
      escapeValue: false,
    },
  });

export default i18n;