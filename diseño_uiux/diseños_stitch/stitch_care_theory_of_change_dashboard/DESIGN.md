---
name: Humanitarian Clarity
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#574237'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#8a7265'
  outline-variant: '#dec1b2'
  surface-tint: '#9b4500'
  primary: '#984300'
  on-primary: '#ffffff'
  primary-container: '#be5600'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb68e'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e2dfde'
  on-secondary-container: '#636262'
  tertiary: '#555c6a'
  on-tertiary: '#ffffff'
  tertiary-container: '#6e7583'
  on-tertiary-container: '#fefcff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbca'
  primary-fixed-dim: '#ffb68e'
  on-primary-fixed: '#331200'
  on-primary-fixed-variant: '#763300'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#dce2f3'
  tertiary-fixed-dim: '#c0c7d6'
  on-tertiary-fixed: '#151c27'
  on-tertiary-fixed-variant: '#404754'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
  section-gap: 64px
---

## Brand & Style

The design system is anchored in the core values of transparency, urgency, and human dignity. It prioritizes a **Minimalist** aesthetic to ensure that critical humanitarian data and narratives are never obscured by visual noise. The target audience includes field coordinators, donors, and administrative stakeholders who require immediate clarity and a sense of calm efficiency.

The visual language utilizes expansive whitespace to create a "breathing" interface, reducing cognitive load during high-stakes decision-making. By stripping away unnecessary borders and ornaments, the focus remains entirely on the impact of the work. The emotional response is one of trust and professionalism, balanced by the warmth of a singular, energetic accent color that represents action and hope.

## Colors

The palette is intentionally restrained to maintain a high-end, editorial feel. 

- **Primary (#E36F1E):** Reserved exclusively for high-priority actions, active navigation states, and critical data points. This "CARE Orange" serves as a beacon of action against the neutral backdrop.
- **Background (#FFFFFF):** The canvas is pure white to maximize the "seamless header" effect and allow content to float naturally.
- **Neutrals:** A scale of cool grays is used for secondary text and subtle surface variations. 
- **Functional Colors:** Success (Green), Warning (Amber), and Error (Red) should be used sparingly and in desaturated tones to prevent them from clashing with the primary orange accent.

## Typography

The design system utilizes **Inter** for all levels to ensure maximum legibility and a modern, systematic feel across all Spanish-language content. 

- **Headlines:** Use a tighter letter-spacing for large displays to create a solid, authoritative presence. 
- **Body Text:** Standard weight is 400. Ensure a generous line height (1.5x minimum) to accommodate longer Spanish word constructions comfortably.
- **Labels:** Utilize medium weights (500) and slight tracking for upper-case labels to distinguish them from body copy without relying on color.
- **Hierarchy:** Use size and weight rather than different typefaces to maintain the minimalist philosophy.

## Layout & Spacing

This design system uses a **Fixed Grid** model for desktop to ensure data visualizations and dashboards remain structured and predictable.

- **Grid:** A 12-column system with a 24px gutter.
- **Margins:** Large outer margins (40px on desktop) reinforce the sense of "luxury" and focus within the humanitarian context.
- **Seamless Integration:** Headers do not use borders. Instead, they rely on a change in background color (White to Ultra-Light Gray) or purely on vertical rhythm and spacing to define the transition from navigation to content.
- **Mobile Adaptivity:** On mobile devices, margins shrink to 16px, and the grid collapses to a single column. "Headline-lg" scales down to 24px to maintain readability without excessive wrapping.

## Elevation & Depth

Depth is achieved through **Ambient Shadows** and tonal layering rather than lines or harsh borders.

- **Surfaces:** Main dashboard cards and containers use a very soft, diffused shadow (0px 4px 20px rgba(0,0,0,0.04)) to lift them off the white background.
- **Interactions:** Upon hover, cards may increase their shadow slightly (0px 8px 30px rgba(0,0,0,0.08)) to indicate interactivity.
- **No Dividers:** Horizontal and vertical lines are strictly avoided. Use spacing (vertical rhythm) or subtle tonal shifts in background fills to separate sections.
- **Overlays:** Modals and dropdowns use a slightly more pronounced shadow with a soft backdrop blur to maintain the clean, "glass-adjacent" feel without being fully translucent.

## Shapes

The shape language is **Rounded**, conveying a sense of approachability and modern care. 

- **Base Radius:** Standard components (buttons, input fields) use a 0.5rem (8px) radius.
- **Large Components:** Dashboard cards and containers use 1rem (16px) to emphasize the soft, welcoming nature of the interface.
- **Pills:** Status indicators (Chips) and search bars may use a full pill shape (100px) to distinguish them from primary action buttons.

## Components

- **Buttons:** The primary button is solid CARE Orange (#E36F1E) with white text. Secondary buttons should be ghost-style with a subtle gray border or a light gray fill.
- **Cards:** Cards are the primary container. They must have no border, a white background, and the "Level 2" roundedness. Use generous padding (24px or 32px) inside cards.
- **Inputs:** Text fields use a light gray background (#F3F4F6) with no border. On focus, they transition to a white background with a subtle primary orange glow.
- **Impact Metrics:** Large numerical displays (e.g., "Personas Ayudadas") should use the `display-lg` typography in the primary color to draw immediate attention.
- **Donation/Progress Bars:** Use a thick, rounded track in light gray with the progress indicated in CARE Orange. Avoid "striped" or "animated" fills to maintain the minimalist aesthetic.
- **Navigation:** The sidebar or top-nav is seamless. Active links are indicated by a bold weight and a small orange dot or a vertical pill-indicator on the left, rather than a full background block.