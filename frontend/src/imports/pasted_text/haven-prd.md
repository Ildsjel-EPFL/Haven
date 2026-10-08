# Product Requirements Document (PRD)

**Project Name:** Haven – Domestic Violence Crisis Support Demo

**Document Status:** Ready for Review

**Target Delivery:** Interactive Demo / Prototype

**Audience:** Front-End Engineers, UX/UI Designers, Safety Auditors

---

## 1. Executive Summary & Purpose

The goal of this project is to build a high-fidelity demo interface for a domestic violence support web portal. The application must prioritize **victim safety, psychological calm, and rapid access to crisis intervention**.

Unlike conventional web applications, this interface operates under the constraint that the user may be in imminent danger or browsing under surveillance. Every aesthetic and architectural decision balances trauma-informed design with life-saving utility.

---

## 2. Target Audience & Core Personas

* **Primary User (Crisis Seeker):** An individual experiencing domestic abuse needing immediate shelter contacts, safety planning, or helpline numbers under extreme time pressure and cognitive distress.
* **Secondary User (Information Seeker):** A friend, family member, or caseworker looking up legal rights, warning signs, and local resources on behalf of a victim.
* **Adversary Profile (The Abuser):** May monitor browser history, perform shoulder-surfing, or inspect open device tabs unexpectedly.

---

## 3. Brand & Visual Design Specifications

The interface implements the custom trauma-informed purple and orange design tokens established for the project.

### 3.1 Design System Tokens

| Token Name | Hex Value | Semantic Role | WCAG Compliance Target |
| --- | --- | --- | --- |
| `--color-surface-base` | `#FBF9F7` | Canvas background, off-white card fills | Base surface |
| `--color-text-primary` | `#201B24` | Primary body typography, high contrast | **AAA** (16.2:1 against Base) |
| `--color-brand-primary` | `#322544` | Structural headers, navigation bar, card outlines | **AAA** (11.4:1 against Base) |
| `--color-brand-secondary` | `#7A628F` | Supportive chips, category pills, subtle borders | **AA** for large UI/graphics |
| `--color-action-emergency` | `#E26D46` | Quick Exit button, urgent hotline CTA | **AA Large** / UI Components |
| `--color-accent-soft` | `#F9A075` | Highlights, badges on dark containers | **AA** (5.4:1 against Plum) |

### 3.2 Visual Atmosphere & Trauma-Informed Constraints

* **Light-dominant canvas:** Avoids dark mode claustrophobia and halation glare.
* **Generous whitespace:** Reduces cognitive overload; line-height set to `1.6` for long-form reading.
* **Softened corners:** Container border-radius set between `8px` and `12px` to convey gentle approachability rather than clinical sharpness.

---

## 4. Key Functional Requirements

### 4.1 "Quick Exit" / Panic Mechanism (P0 - Critical)

* **Persistent Visibility:** A high-visibility button (`#E26D46` with bold white text) anchored to the top-right viewport across all scroll positions.
* **Hardware Trigger:** Hitting the `Escape` key (`Esc`) twice consecutively within 500ms immediately executes the quick exit.
* **Redirection Target:** Instantly redirects to a neutral, universally plausible high-traffic site (e.g., `[https://www.weather.com](https://www.weather.com)` or `[https://www.google.com](https://www.google.com)`).
* **History Poisoning/Clearing:** Replaces browser history via `window.location.replace()` so clicking the browser's "Back" button does not return to the support portal.
* **New Tab Fallback:** Closes the current active tab via `window.close()` if script permissions allow.

### 4.2 Discreet Display / "Camouflage Mode" (P1 - High)

* **Disguise Toggle:** A single-click switch in the utility bar labeled **"Discreet View"** or **"Mask Screen"**.
* **Visual Transform:** Immediately hides crisis-specific branding, swapping headlines to look like a generic lifestyle/recipe blog or neutral search results page, while retaining access to emergency dials.
* **Tab Masking:** Changes the browser tab's `document.title` to `"Quick Pasta Recipes | Home Chef"` and switches the favicon to a generic icon.

### 4.3 Direct Crisis Connect (P0 - Critical)

* **1-Tap Direct Dial:** Prominent click-to-call card for national/local hotlines (`tel:` protocol).
* **Silent Chat Launcher:** Floating action widget offering encrypted SMS or silent live web chat with an immediate "Delete conversation" option.
* **No Call-Logging Notice:** Plain-text micro-copy warning users that standard phone calls may appear on itemized mobile bills, advising burner phones or public lines when possible.

### 4.4 Interactive Safety Planning Wizard (P1 - High)

* **Step-by-Step Flow:** Micro-checklists broken into 3 actionable sections:
1. *Preparing to Leave* (essential documents, medications, spare keys).
2. *During an Incident* (safe rooms with multiple exits, avoiding kitchens/bathrooms).
3. *Digital Safety* (securing location sharing, incognito browsing, private accounts).


* **Zero Client-Side Persistence:** Form selections and checklist states must **never** be saved to `localStorage`, cookies, or session storage to prevent abuser discovery.

---

## 5. Information Architecture & Demo Wireframe Flow

```
+-------------------------------------------------------------------------------+
|  HAVEN  [ Helpline: 1-800-799-SAFE ]         [ Camouflage View ] [ QUICK EXIT ]|
+-------------------------------------------------------------------------------+
|                                                                               |
|  [ Emergency Notice: Safe browsing tips & how to clear your cache ]           |
|                                                                               |
|  HERO SECTION                                                                 |
|  "You Are Not Alone. Free, Confidential Support 24/7."                        |
|  [ Call Hotline Now (tel) ]     [ Start Confidential Text / Chat ]            |
|                                                                               |
+-------------------------------------------------------------------------------+
|  SAFETY ESSENTIALS (3-Card Grid)                                              |
|  +----------------------+ +----------------------+ +----------------------+   |
|  | Immediate Escape Plan| | Emergency Housing    | | Legal & Police Rights|   |
|  | Documents & keys     | | Local safe shelters  | | Protective orders    |   |
|  | [ View Checklist ]   | | [ Find Shelters ]    | | [ Read Guide ]       |   |
|  +----------------------+ +----------------------+ +----------------------+   |
+-------------------------------------------------------------------------------+
|  FOOTER (Neutral, muted background)                                           |
|  Quick Exit Reminder | National Hotlines | Instant Cache Clearing Tool        |
+-------------------------------------------------------------------------------+

```

---

## 6. Non-Functional & Technical Requirements

* **Zero Tracking & Analytics:** Strictly **no** third-party ad pixels (Facebook Pixel, Google Analytics advertising features, TikTok tracking) that could trigger retargeting ads about domestic violence on other devices.
* **Performance:** First Contentful Paint (FCP) under 0.8s on 3G mobile networks. Assets must be lightweight SVG and vanilla CSS.
* **Accessibility:** Full keyboard navigation support (`Tab`, `Enter`, `Space`, `Esc`) with visible focus outlines (`2px solid #E26D46`). Minimum contrast of 4.5:1 across all readable elements.
* **Responsive Layout:** 100% functional on mobile viewports (320px width minimum), prioritizing single-thumb tap targets (minimum 48x48px).

---

## 7. Demo Milestones & Success Criteria

1. **Phase 1 (Visual Polish):** Implementation of color tokens, typography scales, and responsive layout.
2. **Phase 2 (Safety Mechanics):** Testing the Quick Exit latency (<100ms response time on keypress/click) and history replacement behavior across Safari, Chrome, and Firefox mobile/desktop.
3. **Phase 3 (User Testing):** Heuristic review by a trauma-informed specialist and safety audit.