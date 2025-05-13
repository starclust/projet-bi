import { Component } from '@angular/core';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';

@Component({
  selector: 'app-finance-manager',
  templateUrl: './finance-manager.component.html',
  styleUrls: ['./finance-manager.component.css']
})
export class FinanceManagerComponent {
showPowerBI: boolean = true;
  showPrediction: boolean = false;
 
  powerBIUrl: SafeResourceUrl;
  predictionUrl: SafeResourceUrl;

  constructor(private sanitizer: DomSanitizer) {
    // Mets ici ton URL Power BI officielle
    this.powerBIUrl = this.sanitizer.bypassSecurityTrustResourceUrl(
      'https://app.powerbi.com/reportEmbed?reportId=caa32660-1833-40c8-aae9-a3d332407c92&autoAuth=true&ctid=604f1a96-cbe8-43f8-abbf-f8eaf5d85730'
    );

    // Mets ici l'URL de ton serveur Flask déployé
    this.predictionUrl = this.sanitizer.bypassSecurityTrustResourceUrl(
      'http://127.0.0.1:5002'
    );
  }

  showPowerBIView(): void {
    this.showPowerBI = true;
    this.showPrediction = false;
  }

  showPredictionView(): void {
    this.showPowerBI = false;
    this.showPrediction = true;
  }
}
