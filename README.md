## 📊 Modelo de Regresión LTV & Explicabilidad con SHAP

Para predecir el Valor del Cliente a 12 Meses (`FutureLTV_12M`), se optimizó un algoritmo **XGBoost Regressor** en escala logarítmica ($\log(1+y)$) mediante **Optuna** ($50$ iteraciones).

### 🎯 Resultados de Rendimiento
* **MAE:** $126.37 USD *(Reducción del error en $2.38 USD tras optimización)*
* **R² Score:** 0.5222 *(escala real en USD)*
* **MAE Log:** 0.5139 | **R² Log:** 0.6095

---

### 🔍 Hallazgos Principales de Negocio (Interpretación SHAP)

![SHAP Summary](docs/images/shap_summary.png)

1. **Flexibilidad Contractual vs. Retención Financiera:** 
   El factor con mayor peso negativo sobre el LTV es el contrato mes a mes (`ContractType_Month-to-Month`). Convertir a estos clientes a contratos de 1 o 2 años es la palanca comercial con mayor impacto estratégico.
2. **Ticket Promedio (`log_MonthlyCharges`):** 
   Existe una correlación positiva directa: cuotas mensuales más elevadas incrementan de forma consistente la proyección del LTV a 12 meses.
3. **Validación de Feature Engineering (`InactivityRiskIndex`):** 
   La variable sintética creada en la Fase 1 demostró ser un predictor clave (+0.08 impacto medio SHAP), confirmando que la combinación de días sin login y tickets de soporte anticipa caídas en la monetización.

---

### 🚀 Recomendaciones Operativas para el Equipo Comercial
* **Campañas de Migración de Contrato:** Incentivar a usuarios *Month-to-Month* con descuentos anuales para proteger la facturación a largo plazo.
* **Alertas Tempranas:** Activar protocolos de re-engagement cuando el `InactivityRiskIndex` supere el percentil 75.