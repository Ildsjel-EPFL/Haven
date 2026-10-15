import React, { useEffect, useState } from "react";
import { useTranslation, Trans } from 'react-i18next'

const QUICK_EXIT_URL = "https://www.youtube.com"

function quickExit() {
  window.location.replace(QUICK_EXIT_URL)
}

export const { t, i18n } = useTranslation();
  const currentLang = i18n.language;

// Icons (Inline SVG)
const IconEyeOff = ({ size = 24, className = "" }) => (
  <svg
    width={size}
    height={size}
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <path d="M9.88 9.88a3 3 0 1 0 4.24 4.24" />
    <path d="M10.73 5.08A10.43 10.43 0 0 1 12 5c7 0 10 7 10 7a13.16 13.16 0 0 1-1.67 2.68" />
    <path d="M6.61 6.61A13.526 13.526 0 0 0 2 12s3 7 10 7a9.74 9.74 0 0 0 5.39-1.61" />
    <line x1="2" x2="22" y1="2" y2="22" />
  </svg>
)
const IconShieldAlert = ({ size = 24, className = "" }) => (
  <svg
    width={size}
    height={size}
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
    <path d="M12 8v4" />
    <path d="M12 16h.01" />
  </svg>
)
const IconAlertTriangle = ({ size = 24, className = "" }) => (
  <svg
    width={size}
    height={size}
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z" />
    <path d="M12 9v4" />
    <path d="M12 17h.01" />
  </svg>
)
const IconPhoneCall = ({ size = 24, className = "" }) => (
  <svg
    width={size}
    height={size}
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z" />
    <path d="M14.05 2a9 9 0 0 1 8 7.94" />
    <path d="M14.05 6A5 5 0 0 1 18 10" />
  </svg>
)
const IconMessageCircle = ({ size = 24, className = "" }) => (
  <svg
    width={size}
    height={size}
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z" />
  </svg>
)
const IconFileText = ({ size = 24, className = "" }) => (
  <svg
    width={size}
    height={size}
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
    <polyline points="14 2 14 8 20 8" />
    <line x1="16" x2="8" y1="13" y2="13" />
    <line x1="16" x2="8" y1="17" y2="17" />
    <line x1="10" x2="8" y1="9" y2="9" />
  </svg>
)
const IconHome = ({ size = 24, className = "" }) => (
  <svg
    width={size}
    height={size}
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" />
    <polyline points="9 22 9 12 15 12 15 22" />
  </svg>
)
const IconShield = ({ size = 24, className = "" }) => (
  <svg
    width={size}
    height={size}
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
  </svg>
)
const IconX = ({ size = 24, className = "" }) => (
  <svg
    width={size}
    height={size}
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <path d="M18 6 6 18" />
    <path d="m6 6 12 12" />
  </svg>
)

export default function App() {
  const [isCamouflage, setIsCamouflage] = useState(false)
  const [chatOpen, setChatOpen] = useState(false)
  const { t } = useTranslation()

  // Quick Exit: Double ESC
  useEffect(() => {
    let lastEsc = 0
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        const now = Date.now()
        if (now - lastEsc < 500) {
          quickExit()
        }
        lastEsc = now
      }
    }
    window.addEventListener("keydown", handleKeyDown)
    return () => window.removeEventListener("keydown", handleKeyDown)
  }, [])

  // Camouflage Mode Side Effects
  useEffect(() => {
    if (isCamouflage) {
      document.title = "Recettes de Pâtes Rapides | Chef à la Maison"
      const link = document.querySelector(
        "link[rel~='icon']",
      ) as HTMLLinkElement
      if (link) {
        link.href = "https://www.google.com/favicon.ico"
      }
    } else {
      document.title = "Haven | Soutien en cas de crise"
      const link = document.querySelector(
        "link[rel~='icon']",
      ) as HTMLLinkElement
      if (link) {
        link.href = "/favicon.svg"
      }
    }
  }, [isCamouflage])

  if (isCamouflage) {
    return (
      <div className="min-h-screen bg-white">
        <header className="flex justify-between items-center pt-10 pb-4 px-4 sm:p-6 border-b border-gray-200">
          <div className="font-serif text-xl sm:text-2xl text-gray-800">
            {t("camouflage_page.title")}
          </div>
          <div className="flex gap-2 sm:gap-4 items-center">
            <button
              onClick={() => setIsCamouflage(false)}
              className="text-xs sm:text-sm text-gray-500 hover:text-gray-900 min-h-[48px] px-1"
            >
              <span className="hidden sm:inline">Quitter la vue</span>
              <span className="inline sm:hidden">Retour</span>
            </button>
            <button
              onClick={quickExit}
              className="bg-destructive text-destructive-foreground px-4 py-2 sm:px-4 sm:py-2 text-sm sm:text-base font-bold rounded-radius uppercase tracking-wide hover:opacity-90 shadow-md cursor-pointer min-h-[48px] flex items-center justify-center"
            >
              {t("camouflage_page.quick_exit")}
            </button>
          </div>
        </header>
        <main className="w-full mx-auto p-4 sm:p-8 max-w-4xl">
          <h1 className="text-3xl sm:text-4xl font-serif mb-4 sm:mb-6 text-gray-900">
            {t("camouflage_page.recipe_title")}
          </h1>
          <p className="text-gray-700 mb-6 text-base sm:text-lg">
            {t("camouflage_page.recipe_description")}
          </p>
          <div className="bg-gray-100 p-5 sm:p-6 rounded-xl">
            <h2 className="text-xl sm:text-2xl font-serif mb-4">{t("camouflage_page.ingredients")}</h2>
            <ul className="list-disc pl-5 space-y-2 text-gray-700 text-sm sm:text-base">
              <Trans 
              i18nKey="camouflage_page.ingredients_list" 
              components={{ 
                li: <li /> 
              }} 
            />
            </ul>
          </div>
        </main>
      </div>
    )
  }

  return (
    <div className="min-h-screen flex flex-col relative pb-24">
      {/* Quick Exit Floating Header (Optimized for mobile: Bottom-right FAB, moves up if chat is open) */}
      <div className={`fixed z-[100] flex flex-col sm:flex-row items-end sm:items-center gap-3 transition-all duration-300 pointer-events-none ${
        chatOpen 
          ? 'top-20 right-4 sm:top-4 sm:bottom-auto' 
          : 'bottom-6 right-4 sm:bottom-auto sm:top-4'
      }`}>
        <button
          onClick={() => setIsCamouflage(true)}
          className="pointer-events-auto flex items-center justify-center gap-2 bg-white/95 backdrop-blur border border-border text-primary px-4 py-3 sm:px-4 sm:py-2 rounded-full sm:rounded-radius shadow-lg sm:shadow-sm hover:bg-gray-50 transition-colors cursor-pointer min-h-[48px]"
          title="Masquer cette page"
        >
          <IconEyeOff size={20} />
          <span className="hidden sm:inline font-medium">Vue Camouflage</span>
        </button>
        <button
          onClick={quickExit}
          className="pointer-events-auto bg-destructive text-destructive-foreground px-5 py-3 sm:px-6 sm:py-3 text-sm sm:text-base font-bold rounded-full sm:rounded-radius uppercase tracking-wider shadow-xl hover:opacity-90 flex items-center justify-center gap-2 transition-transform active:scale-95 cursor-pointer min-h-[48px]"
          title="Appuyez deux fois sur Échap pour quitter"
        >
          <IconShieldAlert size={20} />
          <span>Sortie Rapide</span>
        </button>
      </div>

      {/* Top Warning Banner */}
      <div className="bg-primary text-primary-foreground pt-14 pb-2 sm:py-3 px-4 sm:px-6 text-xs sm:text-sm flex justify-center text-center">
        <p>
          <IconAlertTriangle
            size={14}
            className="inline-block mr-1 sm:mr-2 mb-1"
          />
          <strong>Avis d'urgence :</strong> L'utilisation d'Internet peut être
          surveillée. Apprenez à{" "}
          <a href="#" className="underline hover:text-accent">
            effacer votre historique
          </a>
          .
        </p>
      </div>

      {/* Navigation */}
      <header className="px-4 sm:px-8 py-4 sm:py-6 flex justify-between items-center max-w-7xl mx-auto w-full">
        <div className="text-2xl sm:text-3xl font-bold text-primary tracking-tight">
          HAVEN
        </div>
        <div className="text-secondary font-medium items-center gap-2 text-sm sm:text-base hidden sm:flex">
          Assistance :{" "}
          <a
            href="tel:1-800-799-7233"
            className="text-primary hover:underline font-bold text-base sm:text-lg"
          >
            1-800-799-SAFE
          </a>
        </div>
      </header>

      {/* Hero Section */}
      <main className="flex-grow flex flex-col items-center px-4 md:px-8 mt-6 sm:mt-12 w-full max-w-7xl mx-auto">
        <div className="text-center max-w-3xl mb-10 sm:mb-16">
          <h1 className="text-3xl sm:text-4xl md:text-6xl font-bold text-primary mb-4 sm:mb-6 leading-tight">
            {t("landing_page.hero_title")}
          </h1>
          <p className="text-base sm:text-xl text-primary/80 mb-8 sm:mb-10 max-w-2xl mx-auto">
            {t("landing_page.hero_description")}
          </p>
          <div className="flex flex-col sm:flex-row gap-3 sm:gap-4 justify-center w-full">
            <a
              href="tel:1-800-799-7233"
              className="bg-primary text-primary-foreground w-full sm:w-auto px-6 py-4 rounded-radius font-semibold text-base sm:text-lg hover:opacity-90 flex items-center justify-center gap-3 shadow-md min-h-[56px]"
            >
              <IconPhoneCall size={24} />
              Appeler la ligne d'assistance
            </a>
            <button
              onClick={() => setChatOpen(true)}
              className="bg-white border-2 border-primary text-primary w-full sm:w-auto px-6 py-4 rounded-radius font-semibold text-base sm:text-lg hover:bg-primary/5 flex items-center justify-center gap-3 shadow-sm cursor-pointer min-h-[56px]"
            >
              <IconMessageCircle size={24} />
              Chat confidentiel
            </button>
          </div>
          <p className="mt-4 text-xs sm:text-sm text-secondary/80 px-2">
            Remarque : Les appels téléphoniques standard peuvent apparaître sur
            les factures mobiles. Utilisez une ligne publique si vous êtes
            surveillé(e).
          </p>
        </div>

        {/* Safety Essentials Grid */}
        <div className="w-full">
          <h2 className="text-xl sm:text-2xl font-bold text-primary mb-4 sm:mb-8 border-b border-border/50 pb-3 sm:pb-4">
            Redirection
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 sm:gap-6">
            {/* Card 1 */}
            <div className="bg-card text-card-foreground p-5 sm:p-8 rounded-xl shadow-sm border border-border/30 hover:border-accent transition-colors flex flex-col h-full">
              <div className="bg-accent/20 w-10 h-10 sm:w-12 sm:h-12 rounded-full flex items-center justify-center text-accent-foreground mb-4 sm:mb-6">
                <IconFileText size={20} className="sm:w-6 sm:h-6" />
              </div>
              <h3 className="text-lg sm:text-xl font-bold mb-2 sm:mb-3 text-primary">
                Plan de Fuite Immédiat
              </h3>
              <p className="text-primary/70 mb-4 sm:mb-6 flex-grow text-sm sm:text-base">
                Une liste de contrôle des documents essentiels, des clés et des
                médicaments à rassembler si vous devez partir rapidement.
              </p>
              <SafetyChecklistModal
                title="Plan de Fuite Immédiat"
                items={[
                  "Pièce d'identité (Permis de conduire, Passeport)",
                  "Certificats de naissance pour vous et vos enfants",
                  "Médicaments et ordonnances",
                  "Clés de rechange (voiture et maison)",
                  "Argent liquide et cartes de crédit",
                ]}
              />
            </div>

            {/* Card 2 */}
            <div className="bg-card text-card-foreground p-5 sm:p-8 rounded-xl shadow-sm border border-border/30 hover:border-accent transition-colors flex flex-col h-full">
              <div className="bg-secondary/10 w-10 h-10 sm:w-12 sm:h-12 rounded-full flex items-center justify-center text-secondary mb-4 sm:mb-6">
                <IconHome size={20} className="sm:w-6 sm:h-6" />
              </div>
              <h3 className="text-lg sm:text-xl font-bold mb-2 sm:mb-3 text-primary">
                Hébergement d'Urgence
              </h3>
              <p className="text-primary/70 mb-4 sm:mb-6 flex-grow text-sm sm:text-base">
                Trouvez des refuges sûrs et des options d'hébergement d'urgence
                dans votre région immédiate.
              </p>
              <button className="text-primary font-bold hover:text-accent w-fit flex items-center gap-1 group cursor-pointer min-h-[48px] sm:min-h-0 text-sm sm:text-base">
                Trouver des refuges{" "}
                <span className="group-hover:translate-x-1 transition-transform">
                  →
                </span>
              </button>
            </div>

            {/* Card 3 */}
            <div className="bg-card text-card-foreground p-5 sm:p-8 rounded-xl shadow-sm border border-border/30 hover:border-accent transition-colors flex flex-col h-full">
              <div className="bg-primary/10 w-10 h-10 sm:w-12 sm:h-12 rounded-full flex items-center justify-center text-primary mb-4 sm:mb-6">
                <IconShield size={20} className="sm:w-6 sm:h-6" />
              </div>
              <h3 className="text-lg sm:text-xl font-bold mb-2 sm:mb-3 text-primary">
                Droits Légaux et Police
              </h3>
              <p className="text-primary/70 mb-4 sm:mb-6 flex-grow text-sm sm:text-base">
                Comprenez vos options pour les ordonnances de protection, les
                signalements aux forces de l'ordre et vos droits légaux.
              </p>
              <button className="text-primary font-bold hover:text-accent w-fit flex items-center gap-1 group cursor-pointer min-h-[48px] sm:min-h-0 text-sm sm:text-base">
                Lire le guide{" "}
                <span className="group-hover:translate-x-1 transition-transform">
                  →
                </span>
              </button>
            </div>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="mt-12 sm:mt-20 border-t border-border/20 bg-card py-8 sm:py-12 px-4 sm:px-6">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-4 sm:gap-6 text-center md:text-left">
          <div className="text-secondary font-medium text-sm sm:text-base">
            N'oubliez pas : Appuyez deux fois sur ÉCHAP ou cliquez sur QUITTER
            pour partir immédiatement.
          </div>
          <div className="flex flex-col sm:flex-row gap-3 sm:gap-6 text-sm text-primary/70 font-medium">
            <a
              href="#"
              className="hover:text-primary min-h-[32px] sm:min-h-0 flex items-center justify-center"
            >
              Lignes d'Assistance Nationales
            </a>
            <a
              href="#"
              className="hover:text-primary min-h-[32px] sm:min-h-0 flex items-center justify-center"
            >
              Outil d'Effacement de Cache
            </a>
          </div>
        </div>
      </footer>

      {/* Floating Chat Widget (Bottom Sheet on Mobile) */}
      {chatOpen && (
        <div className="fixed bottom-0 right-0 sm:bottom-6 sm:right-6 w-full sm:w-80 bg-white sm:rounded-xl rounded-t-xl shadow-2xl border border-border overflow-hidden z-40 flex flex-col">
          <div className="bg-primary text-primary-foreground p-3 sm:p-4 flex justify-between items-center">
            <div className="font-bold flex items-center gap-2">
              <IconShield size={16} /> Chat Sécurisé
            </div>
            <button
              onClick={() => setChatOpen(false)}
              className="hover:bg-primary-foreground/20 p-2 rounded cursor-pointer min-h-[48px] min-w-[48px] flex items-center justify-center"
            >
              <IconX size={20} />
            </button>
          </div>
          <div className="h-[40vh] sm:h-64 p-3 sm:p-4 bg-gray-50 flex flex-col gap-3 overflow-y-auto">
            <div className="bg-gray-200 text-gray-800 p-3 rounded-lg rounded-tl-none w-[90%] sm:w-5/6 text-sm">
              Bonjour. Vous êtes connecté(e) à une Intelligence Artificielle sécurisée
              et confidentielle. Comment pouvons-nous vous aider ?
            </div>
          </div>
          <div className="p-3 bg-white border-t border-gray-200 flex gap-2">
            <input
              type="text"
              placeholder="Tapez votre message..."
              className="flex-grow border border-gray-300 rounded-md px-3 py-2 text-base focus:outline-none focus:border-primary min-h-[48px]"
            />
            <button className="bg-primary text-primary-foreground px-4 rounded-md font-bold text-sm cursor-pointer min-h-[48px]">
              Envoyer
            </button>
          </div>
          <div className="bg-gray-100 p-2 text-center">
            <button
              onClick={() => setChatOpen(false)}
              className="text-xs font-semibold text-destructive hover:underline flex items-center justify-center gap-1 w-full cursor-pointer min-h-[32px] sm:min-h-[40px]"
            >
              <IconAlertTriangle size={14} /> Supprimer la conversation et
              fermer
            </button>
          </div>
        </div>
      )}
    </div>
  )
}

function SafetyChecklistModal({
  title,
  items,
}: {
  title: string
  items: string[]
}) {
  const [isOpen, setIsOpen] = useState(false)
  const [checkedItems, setCheckedItems] = useState<Record<number, boolean>>({})

  const handleOpen = () => {
    setCheckedItems({})
    setIsOpen(true)
  }

  return (
    <>
      <button
        onClick={handleOpen}
        className="text-primary font-bold hover:text-accent w-fit flex items-center gap-1 group cursor-pointer min-h-[48px] sm:min-h-0 text-sm sm:text-base"
      >
        Voir la liste de contrôle{" "}
        <span className="group-hover:translate-x-1 transition-transform">
          →
        </span>
      </button>

      {isOpen && (
        <div className="fixed inset-0 bg-black/60 backdrop-blur-sm z-[100] flex items-end sm:items-center justify-center sm:p-4">
          <div className="bg-white rounded-t-2xl sm:rounded-xl shadow-2xl max-w-lg w-full overflow-hidden flex flex-col h-[85vh] sm:h-auto sm:max-h-[90vh]">
            <div className="p-4 sm:p-6 border-b border-border/30 flex justify-between items-center bg-surface-base sticky top-0 z-10">
              <h3 className="text-xl sm:text-2xl font-bold text-primary pr-4">
                {title}
              </h3>
              <button
                onClick={() => setIsOpen(false)}
                className="text-secondary hover:text-primary p-2 rounded-full hover:bg-gray-100 transition-colors cursor-pointer min-h-[48px] min-w-[48px] flex flex-shrink-0 items-center justify-center"
              >
                <IconX size={24} />
              </button>
            </div>
            <div className="p-4 sm:p-6 overflow-y-auto flex-grow">
              <p className="text-secondary mb-6 text-sm bg-accent/10 p-3 sm:p-4 rounded-lg border border-accent/20">
                <strong>Note de confidentialité :</strong> Cette liste de
                contrôle n'enregistre pas votre progression. Une fois cette
                fenêtre fermée, vos sélections seront effacées.
              </p>
              <div className="space-y-4">
                {items.map((item, idx) => (
                  <label
                    key={idx}
                    className="flex items-start gap-4 cursor-pointer group min-h-[48px] p-1"
                  >
                    <div className="relative mt-0.5 flex-shrink-0">
                      <input
                        type="checkbox"
                        className="peer sr-only"
                        checked={checkedItems[idx] || false}
                        onChange={(e) =>
                          setCheckedItems((prev) => ({
                            ...prev,
                            [idx]: e.target.checked,
                          }))
                        }
                      />
                      <div className="w-6 h-6 border-2 border-secondary rounded flex items-center justify-center peer-checked:bg-primary peer-checked:border-primary transition-colors">
                        {checkedItems[idx] && (
                          <div className="w-3 h-3 bg-white rounded-sm" />
                        )}
                      </div>
                    </div>
                    <span className="text-base sm:text-lg text-primary group-hover:text-primary/80 transition-colors leading-snug">
                      {item}
                    </span>
                  </label>
                ))}
              </div>
            </div>
            <div className="p-4 sm:p-6 border-t border-border/30 bg-gray-50 flex justify-end sticky bottom-0">
              <button
                onClick={() => setIsOpen(false)}
                className="bg-primary text-primary-foreground px-6 py-3 sm:py-2 rounded-radius font-semibold hover:opacity-90 cursor-pointer min-h-[48px] w-full sm:w-auto"
              >
                Terminé
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  )
}
