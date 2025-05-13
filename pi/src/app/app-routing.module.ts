import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TestComponent } from './test/test.component';
import { HomeComponent } from './pages/home/home.component';
import { DashboardComponent } from './dashboard/dashboard.component'; // importe le dashboard
import { AboutusComponent } from './aboutus/aboutus.component';
import { PurchasingManagerComponent } from './purchasing-manager/purchasing-manager.component';
import { SalesManagerComponent } from './sales-manager/sales-manager.component';
import { FinanceManagerComponent } from './finance-manager/finance-manager.component';
import { AdminComponent } from './admin/admin.component';

const routes: Routes = [
  { path: 'test', component: TestComponent },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'aboutus', component: AboutusComponent }, 
  { path: 'purchasing-manager', component: PurchasingManagerComponent },
  {path: 'sales-manager', component: SalesManagerComponent},
  {path: 'finance-manager', component: FinanceManagerComponent},
  { path: 'home', component: HomeComponent },
  { path: 'general-manager', component: AdminComponent },
  { path: '', component: HomeComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
